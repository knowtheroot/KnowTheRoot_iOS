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
    
    NSString *str1 = @"123";
    NSLog(@"address = %p",str1);
    NSString *str2 = [NSString stringWithFormat:@"123"];
    NSLog(@"address = %p",str2);
}


@end
