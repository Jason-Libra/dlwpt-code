"""
import sys

print(sys.path)
# 可以看到sys.path中最前面的就是当前文件所在的目录(有时会显示为'')
# 因此如果导入和build-in模块同名的模块，会导致build-in模块被覆盖
"""

"""
import multiprocessing

print(multiprocessing)
# 可以看到这里导入的是当前目录下的multiprocessing.py，而不是build-in模块multiprocessing
# 同样，下面这行代码也会报错，因为当前路径下的multiprocessing.py并没有Process类

from multiprocessing import Process

# 但是需要注意的是，如果本文件是个jupyter文件，那么sys.path中路径的顺序会发生变化，build-in模块的路径会被放在最前面，也就是出现同名时会导入build-in模块
"""


"""
# 如果使用package.subpackage....module的方式导入模块，那么所有的package和subpackage都会被导入(这意味着所有package和subpackage中的__init__.py文件都会被执行)，但还是只有最后的module会被导入，package和subpackage中的其他mudule并不会被导入

import my_package.my_subpackage.my_subpackage_module
# 可以看到输出有"my_package is imported"和"my_subpackage is imported"
print(my_package)  # 可以看到my_package变量还存在
print(my_package.my_subpackage) # 可以看到my_subpackage变量也还存在
print(my_package.my_subpackage.my_subpackage_module)
"""

"""
# 但是如果使用 from ... import ... as xxx 将最后将导入的module赋值给了其他变量，则只有最后的module会被导入，package和subpackage对应的变量会在导入后被清除

import my_package.my_subpackage.my_subpackage_module as m

# 可以看到输出有"my_package is imported"和"my_subpackage is imported"，意味着导入m的过程中所有的package和subpackage都被导入了
print(m)  # 但是只有m变量会被保留
print(m.__package__)  # 同样，m的__package__属性也会被保留
print(my_package)  # 但是这行代码会报错，因为my_package变量已经被清除
# 同理下面两行也会报错
# print(my_package.my_subpackage)
# print(my_package.my_subpackage.my_subpackage_module)
"""


"""
# 如果package与与其中的module同名
import my_package.my_package

print(my_package)# 可以看到输出的路径是包而不是模块，也就是说如果出现package与其中的module同名，那么导入的是package而不是module

# 如果想要导入module，可以使用 as 语法
import my_package.my_package as m

print(m)  # 可以看到输出的是module而不是package
"""


# relative import与absolute import
