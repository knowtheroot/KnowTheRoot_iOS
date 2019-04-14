//
//  ViewController.m
//  NSStringAndNSMutableString
//
//  Created by 陈家黎 on 2019/4/14.
//  Copyright © 2019 Cooper. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
//    NSString *str1 = @"test";
//    NSString *str2 = [str1 copy];
//    NSString *str3 = [str1 mutableCopy];
//    NSLog(@"str1 address = %p", str1);
//    NSLog(@"str2 address = %p", str2);
//    NSLog(@"str3 address = %p", str3);
    
//    NSString *str1 = @"123";
//    NSString *str2 = @"123";
//    NSLog(@"str1 address = %p", str1);
//    NSLog(@"str2 address = %p", str2);
    
    NSMutableString *mutableStr1 = [[NSMutableString alloc] initWithString:@"123"];
    NSMutableString *mutableStr2 = [[NSMutableString alloc] initWithString:@"123"];
    NSLog(@"mutableStr1 address = %p", mutableStr1);
    NSLog(@"mutableStr2 address = %p", mutableStr2);
    
}


@end
