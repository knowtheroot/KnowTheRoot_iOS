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
