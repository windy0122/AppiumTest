# AppiumTest
简易注册流程，可操作redis数据库获取短信验证码自动输入注册

base层通过调用read函数读取配置文件，找到对应的元素  
page层用于获取界面上每个元素的id、xpath等  
handle层用于封装元素操作方法，如点击按钮，输入文字  
business层用于操作handle层封装的方法  
config用于存放配置文件  
report层用于存放测试报告  
util层用于存放公共方法  


PO模型：  
1、将要测试的页面的元素id、classname等通过相同格式写入ini文件中  
2、通过util层的read_ini.py，读取ini文件，获取配置文件中的元素数据  
3、通过base层的find_element.py文件，调用read_ini文件函数，将获取的元素数据通过split方法分割获取key和value，key即为id、xpath等，value为元素的值    
4、通过page层调用base层的函数，获取当前页面的每个元素（如登录按钮即为login_button）信息，通过return返回，  
5、handle层调用page层return返回的数据，选择该数据的操作方式，是click、send_keys等，  
6、business层调用handle层封装的元素操作方法，来操作该方法，   
7、case层为测试的用例，调用business封装的操作方法，实现测试用例   

