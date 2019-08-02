# AppiumTest
简易注册流程，可操作redis数据库获取短信验证码自动输入注册

base层通过调用read函数读取配置文件，找到对应的元素  
page层用于获取界面上每个元素的id、xpath等  
handle层用于封装元素操作方法，如点击按钮，输入文字  
business层用于操作handle层封装的方法  
config用于存放配置文件  
report层用于存放测试报告  
util层用于存放公共方法  
