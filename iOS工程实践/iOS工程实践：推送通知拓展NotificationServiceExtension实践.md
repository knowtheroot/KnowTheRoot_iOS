![avatar](https://user-gold-cdn.xitu.io/2019/4/11/16a0b75d5c2b0f8e?w=600&h=190&f=jpeg&s=15670)
## 前言

自iOS10 更新以来，Apple 表示这是 iOS 有史以来最大的升级(our biggest release yet)，更加智能开放的Siri、强化应用对3DTouch支持、 HomeKit 、电话拦截及全新设计的通知等等。

iOS 10 中将之前繁杂的推送通知统一成UserNotifications.framework 来集中管理和使用通知功能，还增加一些实用的功能——撤回单条通知、更新已展示通知、中途修改通知内容、在通知中显示多媒体资源、自定义UI等功能。

iOS10推送通知的有以下两个两个扩展框架:
- **UNNotificationServiceExtension（通知服务拓展）**
- **UNNotificationContentExtension（通知内容拓展）**

| 通知拓展 | 特性 |
| ------ | ------ |
| UNNotificationServiceExtension | 在收到通知后，展示通知前，做一些事情的。比如，增加附件，网络请求等。 |
| UNNotificationContentExtension | 可以通过提前配置的categoryIdentifier来定制推送显示的界面 |

## 一、UNNotificationServiceExtension - 通知服务扩展

### 1.什么是UNNotificationServiceExtension？

的主要功能，是让我们在收到**远程推送**的时候，<u>在推送展示之前对其进行修改</u>，因为我们收到远程推送之前会先去执行Service Extension中的代码，这样就可以在收到远程推送展示之前做一些操作。

### 2.UNNotificationServiceExtension的作用

通知服务拓展能做什么？举个例子：  
#### 1.更改推送内容 
通过远程推送，推送的内容的title="1"，我可以在收到推送将要显示之前将标题修改成title="2",那么推送条展示的title就是2。  
#### 2.对推送内容加解密
在发送推送的时候发送一段用公钥加密的内容，然后设备收到推送之后，用私钥进行解密然后再去展示。例如开发者不想让第三方推送sdk（极光推送等）知晓推送内容，则可以采用通知服务拓展。  
#### 3.推送事件响应
在推送发送时，可以使用服务拓展对通知的状态（例如到达率）做统计。  
#### 4.富媒体下载
当远程推送需要展示多媒体的时候，也需要在这下载，下载完毕之后，获取本地下载文件路径再进行展示。对下载附件多媒体得需要Service Extension。

### 3.UNNotificationServiceExtension实践

#### 3.1 创建一个Service Extension
**File -> New -> Target**  
选择拓展
![avatar](https://user-gold-cdn.xitu.io/2019/4/11/16a0b5a3b0c7c3f1?w=721&h=510&f=png&s=74746)
随后点击创建拓展即可，发现此时在项目中出现“xxxServiceExtension”的文件夹。  
文件夹中包含了推送拓展类NotificationService。  
![avatar](https://user-gold-cdn.xitu.io/2019/4/11/16a0b6a785464631?w=331&h=61&f=png&s=8235)
#### 3.2 测试
第一步，选择target为extension，运行项目：
![](https://user-gold-cdn.xitu.io/2019/4/12/16a0f641622a72b7?w=452&h=38&f=png&s=17152)
第二步，选择当前项目
![](https://user-gold-cdn.xitu.io/2019/4/12/16a0f7478b3d217f?w=440&h=407&f=png&s=71211)
  
第三步，在NotificationService.m中的didReceiveNotificationRequest中添加断点：

![](https://user-gold-cdn.xitu.io/2019/4/12/16a0f75e5408304b)
第四步，发个远程推送，注意，本地推送是没反应的。

#### 3.2 远程推送相关注意事项
相对于普通推送，推送服务拓展payload的内容基本相同，举个例子：  
```
{
  "aps":{
    "alert":{
      "title":"iOS 10 title",
      "subtitle":"iOS 10 subtitle",
      "body":"iOS 10 body"
    },
    "mutable-content":1,
    "category":"saySomethingCategory",
    "sound":"default",
    "badge":3
  }
}
```
注意，推送内容多了一个**mutable-content**，它表示我们会在接收到通知时对内容进行更改。  
开发者在didReceiveNotificationRequest方法中有**30秒**的时间对推送内容到达前进行处理。例如：
```
- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {
    self.contentHandler = contentHandler;
    self.bestAttemptContent = [request.content mutableCopy];
    
    // Modify the notification content here...
    self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];
    self.bestAttemptContent.body = @"我是新修改的body";
    self.bestAttemptContent.title = @"我是新修改的title";
    self.bestAttemptContent.subtitle = @"我是新修改的subtitle";
    
    self.contentHandler(self.bestAttemptContent);
}
```
#### 3.3 推送测试工具
这里推荐Knuff：
https://github.com/KnuffApp/Knuff

  [参考文献http://www.cocoachina.com/ios/20160628/16833.html](http://www.cocoachina.com/ios/20160628/16833.html)
