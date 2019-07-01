

# Cube

一个用纯文字和命令行来玩的魔方。
缺省是3阶魔方，可以在命令行指定阶数。
运行后显示以下界面：

```
h/help   : Show this usage
random   : Shuffle the magic cube
q/Q/exit : Quit
Multiple commands can be used for below actions:
    U/u  : Rotate the Up    surface clockwise / anti-clockwise
    D/d  : Rotate the Down  surface clockwise / anti-clockwise
    L/l  : Rotate the Left  surface clockwise / anti-clockwise
    R/r  : Rotate the Right surface clockwise / anti-clockwise
    F/f  : Rotate the Front surface clockwise / anti-clockwise
    B/b  : Rotate the Back  surface clockwise / anti-clockwise
    X/x  : Rotate the Magic cube along X-axis clockwise / anti-clockwise
    Y/y  : Rotate the Magic cube along Y-axis clockwise / anti-clockwise
    Z/z  : Rotate the Magic cube along Z-axis clockwise / anti-clockwise
    For example, we can input : RUrURUUr or RuRURURuruRR
----------------------------
        U U U
        U U U
        U U U

L L L   F F F   R R R   B B B
L L L   F F F   R R R   B B B
L L L   F F F   R R R   B B B

        D D D
        D D D
        D D D
----------------------------
```

## 用法(以3阶魔方为例)

###  h/help   : 显示帮助信息
### random   : 打乱魔方 
### q/Q/exit : 退出
### 以下命令用来操作魔方。 可以多个命令同时使用:
    U/u  : 顺时针/逆时针转动魔方的上面
    D/d  : 顺时针/逆时针转动魔方的下面
    L/l  : 顺时针/逆时针转动魔方的左面
    R/r  : 顺时针/逆时针转动魔方的右面
    F/f  : 顺时针/逆时针转动魔方的前面
    B/b  : 顺时针/逆时针转动魔方的后面
    X/x  : 将整个魔方沿X轴方向顺时针/逆时针转动
    Y/y  : 将整个魔方沿Y轴方向顺时针/逆时针转动
    Z/z  : 将整个魔方沿Z轴方向顺时针/逆时针转动

### 举个例子
当魔方显示以下状态（这时处于已复原状态） 时：
```
        U U U
        U U U
        U U U

L L L   F F F   R R R   B B B
L L L   F F F   R R R   B B B
L L L   F F F   R R R   B B B

        D D D
        D D D
        D D D
```
此时输入命令：
```
RUrURUUr
```
实际上就是针对魔方做了以下8个动作：
顺时针旋转右面（R）
顺时针旋转上面（U）
逆时针旋转右面（r）
顺时针旋转上面（U）
顺时针旋转右面（R）
顺时针旋转上面（U）
顺时针旋转上面（U）
逆时针旋转右面（r）
以上操作做完后， 魔方变成以下状态：

```
        F U U
        U U U
        R U B

U B B   U F L   U L L   F R R
L L L   F F F   R R R   B B B
L L L   F F F   R R R   B B B

        D D D
        D D D
        D D D
```
