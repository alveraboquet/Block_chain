[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=4abde3ee-fca0-4628-b87d-8c09939fa5e5
Description=狐狸钱包相关函数
Enable=0
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
//                ▼▼《大漠免费设置》▼▼                //
Const GlobalPath = "C:\紫猫编程学院\dm脚本" //大漠的全局路径,会自动创建该目录,并且自动将所有附件释放到该目录下
Const Contact = "紫猫学院QQ:345911220 官网:zimaoxy.com 微信公众号:zimaoxy-com" //脚本作者联系方式,可以留空
Const dmVer = "3.1233" //大漠版本号,必须带上双引号,3.1233是最后一个免费版,换版本记得修改
Const PicPwd = "123456" //图片密码,可以留空
Const DictPwd = "123456" //字库密码,可以留空
Const DictFiles = "ziku.txt" //设置字库,留空表示不使用字库,如果需要多个字库,以|分隔,比如"xp.txt|win7.txt",默认调用第1个字库
Const setFindX = 1920 //设置所有查找相关命令(比如找图找色找字)的范围右下角x,请根据实际情况调整
Const setFindY = 1080 //设置所有查找相关命令(比如找图找色找字)的范围右下角y,请根据实际情况调整
Const EnableLog = 0 //是否开启日志记录,0为关闭,1为开启,详见按键精灵的LogStart函数
Const CustomDisplayDebug = 0 //是否开启自定义图色调试模式(仅对自己写的CapturePre生效,对模板中的CapturePre无效),0为关闭,1为开启,详见大漠的EnableDisplayDebug函数
Const AllDisplayDebug = 1 //是否开启全部图色调试模式(对自己写的与模板中的CapturePre都生效),0为关闭,1为开启,详见大漠的EnableDisplayDebug函数
//                ▼▼《大漠付费设置》▼▼                //
Const RegCode = "" //大漠付费注册码,请去大漠后台系统查看,留空表示不使用付费功能,仅使用免费功能
Const RegVersion = "" //大漠付费注册中的版本信息(如果你不知道什么用,那么建议留空),注意:长度不能超过10,并且只能包含数字和字母以及小数点,否则会报错!!!
//                ▼▼《注册创建大漠》▼▼                //
Call zmRegDM() //释放所有附件,注册并创建大漠对象dm
Call zmSetDm()//设置大漠常用属性配置
//                ▼▼《开始写脚本吧》▼▼                //
//登录小狐狸钱包 ("12345678")
//Call 进入选钱包界面()
//Call 登录钱包("Account20")
//Call 选择狐狸钱包网络("Rinkeby")
//If Lib.dm.zmWaitStrEx(1749,546, 1884,583,"确认", "ffffff-000000",10) > -1 Then
//    TracePrint "找到确认"
//End if
Function 登录小狐狸钱包(pwd)
    If Lib.dm.zmFindImg("小狐狸插件图片.bmp|小狐狸插件图片2.bmp") > - 1  Then 
        Delay 500
        Call Lib.dm.zmLClick(ImgX, ImgY)
        Delay 500
        If Lib.dm.zmWaitImg("狐狸左上头像.bmp", 30) > - 1  Then 
            Delay 1000
            SayString pwd
            Delay 500
            KeyPress "Enter", 1
            Delay 500
        End If
        If Lib.dm.zmWaitStrEx(1326,67,1880,668,"发送","037dd6-101010",30) > - 1  Then 
            TracePrint "成功打开狐狸钱包"
            登录小狐狸钱包 = 1
        Else 
            If Lib.dm.zmFindStr("明白了", "ffffff-202020") > - 1  Then 
                Delay 500
                Call Lib.dm.zmLClick(StrX, StrY)
                TracePrint "成功打开狐狸钱包,并按明白了"
            ElseIf Lib.dm.zmFindImg("小狐狸新功能.bmp") > - 1  Then
                Call Lib.dm.zmFindImg("小狐狸叉叉.bmp")
                Delay 500
                Call Lib.dm.zmLClick(ImgX, ImgY)
                TracePrint "点击叉叉"
            End If
        End If
    End If
End Function
Function 登录钱包(钱包名)
    Dim i
    //输入钱包序号,去配置文件查找在小狐狸中的钱包名,按照得到的钱包名
    //钱包名 = File.ReadINI(钱包序号, "钱包名", "C:\紫猫编程学院\dm脚本\小狐狸导入进度.ini")
    TracePrint 钱包名
    Call 进入选钱包界面()
    For i = 1 To 100
        If Lib.dm.zmFindStrEx(1324, 69, 1780, 669, 钱包名, "ffffff-101010") > - 1  Then 
            Call Lib.dm.zmLClick(StrX, StrY)
            Delay 1000
            返回值 = Lib.dm.zmOcr(1324,258,1782,314 ,"000000-000000")
            Delay 500
            Exit For
        ElseIf i > 999 Then
            TracePrint "Error没有找到钱包:" & 钱包名
        Else 
            MouseWheel - 1 
            Delay 100
        End If
    Next
    If Lib.dm.zmFindStr("明白了", "ffffff-202020") > - 1  Then 
        Delay 500
        Call Lib.dm.zmLClick(StrX, StrY)
        TracePrint "成功打开狐狸钱包,并按明白了"
    ElseIf Lib.dm.zmFindImg("小狐狸新功能.bmp") > - 1  Then
        Call Lib.dm.zmFindImg("小狐狸叉叉.bmp")
        Delay 500
        Call Lib.dm.zmLClick(ImgX, ImgY)
        TracePrint "点击叉叉"
    End If
    TracePrint 返回值
    登录钱包 = 返回值
End Function
Function 进入选钱包界面()
    If Lib.dm.zmFindStrEx(1324, 69, 1780, 669, "我的账户", "ffffff-101010") > - 1  Then 
        Delay 500
        MoveTo StrX + 300, StrY + 100
        Delay 500
    ElseIf Lib.dm.zmWaitStrEx(1326, 67, 1880, 668, "发送", "037dd6-101010", 10) > - 1  Then
        Delay 1000
        Call Lib.dm.zmLClick(StrX + 170, StrY - 275)
        Delay 1000
        Call 进入选钱包界面()
    Elseif Lib.dm.zmFindImg("小狐狸插件图片2.bmp") > - 1  Then 
        Delay 500
        Call Lib.dm.zmLClick(ImgX, ImgY)
        Delay 500
        If Lib.dm.zmWaitStr("详情|授予", "000000-101010|4d4d4d-101010", 15) > -1 Then
            Call Lib.dm.zmLClick(StrX, StrY)
        End IF
        For 5
            If Lib.dm.zmFindStrEx(1749,546, 1884,583, "拒绝", "037dd6-000000") > - 1  Then 
                TracePrint "找到拒绝"
                Exit For
            Else 
                MouseWheel - 1 
                Delay 100
            End If
        Next
        t1 = timer
        Do While True
            If Lib.dm.zmFindStrEx(1749,546, 1884,583, "拒绝", "037dd6-000000") > - 1 Then
                Call Lib.dm.zmLClick(StrX, StrY)
                Delay 500
            ElseIf timer - t1 > 10 Then
                Exit Do
            Else 
                Exit DO
            End if
        Loop
        Delay 5000
    Elseif Lib.dm.zmWaitImg("小狐狸插件图片.bmp",10) > - 1  Then 
        Delay 500
        Call Lib.dm.zmLClick(ImgX, ImgY)
        Delay 500
        Call 进入选钱包界面()
    End If
End Function
Function 选择狐狸钱包网络(网络名)
    If Lib.dm.zmWaitImg("狐狸左上头像.bmp", 10) > - 1  Then 
        //看是否默认网络
        If Lib.dm.zmWaitStrEx(ImgX, ImgY, ImgX + 330, ImgY + 40, 网络名, "6a737d-101010", 5) > - 1  Then 
            TracePrint "选择默认网络:" & 网络名
        Else 
            Call Lib.dm.zmLClick(ImgX + 180, ImgY + 20)
            Call Lib.dm.zmMove(ImgX+180,ImgY + 300)
            //选择网络
            For 10 
                If Lib.dm.zmWaitStrEx(ImgX, ImgY, ImgX + 340, ImgY + 480, 网络名, "9b9b9b-101010|ffffff-000000", 5) > - 1  Then 
                    Call Lib.dm.zmLClick(StrX, StrY)
                    TracePrint "选择网络:" & 网络名
                    Exit For
                Else 
                    MouseWheel - 1 
                    Delay 100
                    TracePrint "没有找到网络:"&网络名
                End If
            Next
        End If
    ElseIf Lib.dm.zmFindImg("小狐狸插件图片.bmp") > - 1  Then 
        Delay 500
        Call Lib.dm.zmLClick(ImgX, ImgY)
        Delay 500
        Call 选择狐狸钱包网络(网络名)
    End If
End Function
Function 交互确认()
    Dim gas,t1
    //新版模式下
    If Lib.dm.zmWaitStr("详情|授予", "000000-101010|4d4d4d-101010", 15) > - 1  Then 
        Delay 500
        TracePrint "打开了小狐狸交互页面"
        //更改ui
        If Lib.dm.zmFindStrEx(1577, 5, 1919, 603, "Gasfee", "037dd6-000000") > - 1  Then 
            TracePrint "旧版UI 改成新版"
            Call Lib.dm.zmLClick(StrX, StrY)
            If Lib.dm.zmWaitStrEx(1577, 5, 1919, 603, "Gasfee", "4d4d4d-000000", 10) > - 1  Then 
                Call Lib.dm.zmLClick(1611, 446)
                TracePrint "打开新UI"
                If Lib.dm.zmWaitImgEx(1577, 5, 1919, 603, "小狐狸叉号.bmp", 10) > - 1  Then 
                    Call Lib.dm.zmLClick(ImgX, ImgY)
                    Delay 3000
                End If
            End If
        End If
        Delay 3000
        gas = Lib.dm.zmFindStrEx(1577, 5, 1919, 603, "进取|市场|低", "037dd6-101010")
        TracePrint gas
        If gas  = 0  Then 
            TracePrint "当前gas费为高"
        ElseIf gas = 1 Then
            TracePrint "当前gas费为中,选择高gas费"
            Call Lib.dm.zmLClick(StrX, StrY)
            Delay 1000
            Call Lib.dm.zmFindStrEx(1577, 5, 1919, 603, "进取", "24292e-101010")
            Call Lib.dm.zmLClick(StrX, StrY)
        ElseIf gas = 2 Then
            TracePrint "当前gas费为低,选择高gas费"
            Call Lib.dm.zmLClick(StrX, StrY)
            Delay 1000
            Call Lib.dm.zmFindStrEx(1577, 5, 1919, 603, "进取", "24292e-101010")
            Call Lib.dm.zmLClick(StrX, StrY)
        End If
        If Lib.dm.zmWaitStr("详情|授予", "000000-101010|4d4d4d-101010", 15) > -1 Then
            Call Lib.dm.zmLClick(StrX, StrY)
        Else 
            //移动到默认确认位置
            Call Lib.dm.zmMove(1803, 558)
            Delay 500
        End IF
        For 5
            If Lib.dm.zmFindStrEx(1749,546, 1884,583, "确认", "ffffff-101010") > - 1  Then 
                TracePrint "找到确认"
                Delay 3000
                Exit For
            Else 
                MouseWheel - 1 
                Delay 100
            End If
        Next
        For 5
            MouseWheel - 1 
            Delay 100
        Next
        t1 = timer
        Do While True
            If Lib.dm.zmFindStrEx(1749,546, 1884,583, "确认", "ffffff-101010") > - 1 Then
                Call Lib.dm.zmLClick(StrX, StrY)
                Delay 500
            ElseIf timer - t1 > 10 Then
                Exit Do
            Else 
                Exit DO
            End if
        Loop
        If Lib.dm.zmWaitImgEx(1326, 749, 1919, 1077, "小狐狸链上确认头像.bmp", 100) > - 1  Then 
            TracePrint "本次交互成功"
            交互确认 = 1
            Exit Function
        Else 
            交互确认 = -1
            TracePrint "100秒内未交互成功"
            Exit Function
        End If
    End if
End Function
Function 连接钱包()
    Dim i
    If Lib.dm.zmWaitStr("已连接", "6a737d-000000", 10) > -1 Then 
        TracePrint "该浏览器已连接"
    Else 
        If Lib.dm.zmWaitImg("小狐狸对号.bmp", 20) > - 1  Then 
            Call Lib.dm.zmLClick(ImgX, ImgY)
            Delay 500
            Call Lib.dm.zmLClick(ImgX, ImgY)
        End If
        For i = 1 To 500
            If Lib.dm.zmFindStrEx(1577, 8, 1915, 604, "全部选择", "6a737d-000000") > - 1  Then 
                Delay 200
                If Lib.dm.zmFindImgEx(1577, 8, 1915, 604, "小狐狸半选号.bmp") > - 1  Then 
                    Call Lib.dm.zmLClick(ImgX + 5, ImgY + 5)
                    TracePrint "全部选择"
                    Exit For
                    //全部选择
                End If 
            Else 
                MouseWheel 1 
                Delay 100
            End If
        Next
        For i = 1 To 500
            If Lib.dm.zmFindStrEx(1577, 8, 1915, 604, "下一步","ffffff-000000") > - 1  Then 
                Call Lib.dm.zmLClick(StrX,StrY)
                TracePrint "点击下一步"
                Exit For
                //下一步
            ElseIf i = 500 Then
                Call Lib.dm.zmLClick(1821,567)
                TracePrint "点击默认下一步位置"
            Else 
                MouseWheel - 1 
                Delay 100
            End If
        Next
        If Lib.dm.zmWaitStr("连接", "ffffff-000000", 20) > - 1  Then 
            Call Lib.dm.zmLClick(StrX, StrY)
            TracePrint "连接所有钱包地址"
        Else 
            TracePrint "没有找到连接,点击默认连接位置"
            Call Lib.dm.zmLClick(1821,567)
        End If
    End If
End Function
Function 随机更换代理()
    Dim a,b,i,t1,g
    a = Array("香港01","香港02","香港03","香港04","香港05","香港06","香港07","香港08","香港09","香港10","香港11","香港12","香港13","香港14","香港15","香港16","香港17","香港18","香港19","香港20","日本01","日本02","日本03","日本04","日本05","日本06","v1香港01M","v1香港02M","v1香港03M","v1香港04M","v1香港05M","v1新加坡01M","v1新加坡02M","v1新加坡03M","v1新加坡13M","v1新加坡04M","v1新加坡05M","v1日本01M","v1日本02M","v1日本03M","v1日本12M","v1日本04M","v1日本05M","v1香港01原生","v1香港02原生","v1香港03原生","v1香港04原生","v1香港05原生","v1台湾03原生","v1台湾02原生","v1台湾04原生","v1台湾05原生","v1新加坡01原生","v1新加坡02原生","v1新加坡04原生","v1新加坡05原生","HK香港01","HK香港02","HK香港03","HK香港04","HK香港05","HK香港06","HK香港07","HK香港08","HK香港09","HK香港10","HK香港11","HK香港12","HK香港13","HK香港14","HK香港15","HK香港16","HK香港17","HK香港18","HK香港19","HK香港20","HK香港21","HK香港22","HK香港23","HK香港24","HK香港25","SG新加坡01","SG新加坡02","SG新加坡03","SG新加坡04","SG新加坡05","SG新加坡06","SG新加坡07","SG新加坡08","SG新加坡09","SG新加坡10","SG新加坡11","SG新加坡12","SG新加坡13","SG新加坡14","SG新加坡15","SG新加坡16","SG新加坡17","SG新加坡18","SG新加坡19","JP日本01","JP日本02","JP日本03","JP日本04","JP日本05","JP日本06","JP日本07","JP日本08","JP日本09","JP日本10","JP日本11","JP日本12","JP日本13","JP日本14","JP日本15","JP日本16","JP日本17","JP日本18","JP日本19","TW台湾01","TW台湾02","TW台湾03","TW台湾04","TW台湾05","TW台湾06")
    Do While True
        If Lib.dm.zmFindStrEx(9, 967, 149, 1034, "已连接", "000000-000000") > - 1  Then 
            TracePrint "已经打开clash页面"
            Call Lib.dm.zmLClick(StrX+110,StrY)
            Exit DO
        ElseIf Lib.dm.zmFindImg("clash菜单栏图标.bmp|clash右下角图标.bmp") > - 1  Then
            Call Lib.dm.zmLClick(ImgX, ImgY)
            Delay 3000
        End If
    Loop
    bound = UBound(a)
    TracePrint bound
    For i = 1 To 10
        For 20
            MouseWheel  1 
            Delay 100
        Next
        b = Lib.dm.zmRandom(0,bound)
        For g= 1 to 20
            If Lib.dm.zmFindStr(a(b), "000000-000000") > - 1  Then 
                TracePrint a(b)
                Call Lib.dm.zmLClick(StrX,StrY)
                TracePrint "点击下一步"
                Delay 3000
                Exit For
            ElseIf g = 20 Then
                TracePrint "代理没找到"
                Goto A随机更换代理
            Else 
                MouseWheel - 1 
                Delay 100
            End If
        Next
        If Lib.dm.zmFindStrEx(StrX, StrY, StrX + 300, StrY + 30, "超时", "ec0505-000000") > - 1  Then 
            TracePrint "该节点"&a(b)&"不能使用 跳过"
        Else 
            TracePrint "使用该节点" & a(b)
            Call Lib.dm.zmLClick(1839, 11)
            Delay 500
            Exit Function 
        End If
        Rem A随机更换代理
    Next 
    //下一步
End Function
//                ▼▼《大漠函数部分》▼▼                //
Sub zmRegDM()//注册大漠
    Dim PathArr, FatherPath, DebugPath, ver, MsgError, i, ws
    //创建大漠的全局路径文件夹
    If Plugin.File.ExistFile(GlobalPath) = 0 Then
        PathArr = Split(GlobalPath, "\")
        For i = 0 To UBound(PathArr)
            If i = 0 Then
                FatherPath = PathArr(0)
            Else
                FatherPath = FatherPath & "\" & PathArr(i)
                Call Plugin.File.CreateFolder(FatherPath)
                Delay 500
            End If
        Next
    End If
    DebugPath = GlobalPath & "\Debug"
    //开启大漠图色调试模式的情况下，默认每次自动删除Debug截图目录，避免文件夹过大
    If CustomDisplayDebug or AllDisplayDebug Then
        Call Plugin.File.DeleteFolder(DebugPath)
        Delay 2000
    End If
    Call Plugin.File.CreateFolder(DebugPath)
    If EnableLog Then
        LogStart GlobalPath & "\Debug\Error.log"
    End If
    PutAttachment GlobalPath, "*.*" //释放所有文件
    // 插件需要用到atl系统库,有些XP精简系统会把atl.dll精简掉. 为了防止注册失败，这里手动注册一下atl.dll
    set ws=createobject("Wscript.Shell")
    ws.run "regsvr32 atl.dll /s"//这句话如果报错可以不用理会,没关系的
    set ws=nothing
    // 凡是下面这句Call Plugin.RegDll.Reg(GlobalPath & "\dm.dll")报错的同学,
    // 请将大漠压缩包中的RegDll.dll插件文件放到按键精灵Plugin目录下后,重启按键精灵
    Call Plugin.RegDll.Reg(GlobalPath & "\dm.dll")//注册大漠
    Delay 1500
    Set dm = CreateObject("dm.dmsoft")//创建大漠对象
    ver = dm.ver()//获取当前大漠版本
    If ver <> CStr(dmVer) Then
        set dm = nothing
        MsgBox "大漠注册失败，如果是win7或者vista机器，请关闭UAC，并重启，如果依旧无效，请联系" & Contact, 4096, "紫猫编程学院"
        ExitScript
    End If
    TracePrint "大漠注册成功，路径为:" & dm.GetBasePath() & "  版本为:" & dm.ver() & "  请注意,高于3.1233版本的为大漠付费版,必须付费才能使用."
    If RegCode <> "" Then
        //注册付费功能
        dm_ret = dm.Reg(RegCode, RegVersion)
        If dm_ret <> 1 Then
            MsgError = zmRegError(dm_ret)
            MsgBox "付费功能注册失败，原因如下:" & vbcrlf & vbcrlf & MsgError & vbcrlf & vbcrlf & "请将此错误告知" & Contact, 4096, "紫猫编程学院"
            ExitScript
        End If
    End If
End Sub
Sub zmSetDm()//设置大漠
    Dim DictArr, i
    //设置大漠全局路径
    dm.SetPath GlobalPath 
    //设置图片密码,对未加密图片无影响
    dm_ret = dm.SetPicPwd(PicPwd)
    //设置字库
    If DictFiles <> "" Then
        dm_ret = dm.SetDictPwd(DictPwd)
        DictArr = Split(DictFiles, "|")
        For i = 0 To UBound(DictArr)
            dm_ret = dm.SetDict(i, DictArr(i))
        Next
        dm_ret = dm.UseDict(0)
    End If
    //图色调试模式
    If CustomDisplayDebug or AllDisplayDebug Then
        dm.EnableDisplayDebug 1
    End If
End Sub
Function zmRegError(setCode)
    Select Case setCode
    Case - 1 
        zmRegError = "错误代码: " & setCode & vbcrlf & "无法连接网络,(可能防火墙拦截,如果可以正常访问大漠插件网站，那就可以肯定是被防火墙拦截)"
    Case - 2 
        zmRegError = "错误代码: " & setCode & vbcrlf & "进程没有以管理员方式运行. (出现在win7 vista 2008.建议关闭uac)"
    Case 2
        zmRegError = "错误代码: " & setCode & vbcrlf & "余额不足"
    Case 3
        zmRegError = "错误代码: " & setCode & vbcrlf & "绑定了本机器，但是账户余额不足50元"
    Case 4
        zmRegError = "错误代码: " & setCode & vbcrlf & "注册码错误"
    Case 5
        zmRegError = "错误代码: " & setCode & vbcrlf & "你的机器或者IP在黑名单列表中或者不在白名单列表中"
    Case -8
        zmRegError = "错误代码: " & setCode & vbcrlf & "版本附加信息长度超过了10"
    Case -9
        zmRegError = "错误代码: " & setCode & vbcrlf & "版本附加信息里包含了非法字母"
    Case ""
        zmRegError = "错误代码: " & setCode & vbcrlf & "这是不可能返回空的，如果出现空，那肯定是当前使用的版本不对,老的插件里没这个函数导致返回为空.最好参考文档中的标准写法,判断插件版本号"
    Case Else
        zmRegError = "错误代码: " & setCode & vbcrlf &  "未知错误。"
    End Select
End Function
Sub zmUnRegDM()//卸载大漠
    Dim ver, vers, base_path, dm, ws
    Set dm = createobject("dm.dmsoft")
    ver = dm.Ver()
    If Len(ver)>0 Then
        base_path = dm.GetBasePath()
        set dm = Nothing
        Set ws = createobject("Wscript.Shell")
        ws.run "regsvr32 /u /s " & base_path & "dm.dll"
        Delay 2000
        Set ws = Nothing
        Set dm = createobject("dm.dmsoft")
        vers = dm.Ver()
        If Len(vers)=0 Then
            MsgBox "在 " & base_path & " 中卸载大漠" & ver & "版本成功，请重新运行脚本。如果此提示多次出现，请联系" & Contact, 4096, "紫猫编程学院"
        Else
            MsgBox "在 " & base_path & " 中卸载大漠" & ver & "版本失败，请重新运行脚本。如果此提示多次出现，请联系" & Contact, 4096, "紫猫编程学院"
        End If
    Else
        MsgBox "系统未安装大漠，无需卸载大漠，请重新运行脚本。如果此提示多次出现，请联系" & Contact, 4096, "紫猫编程学院"
    End If
    set dm = Nothing
    ExitScript
End Sub
Sub zmBindForeground(setHwnd)//前台绑定
    Dim getError
    dm_ret = dm.BindWindow(setHwnd, "normal", "normal", "normal", 0)
    If dm_ret = 0 Then
        getError = dm.GetLastError()
        TracePrint "句柄" & setHwnd & "前台绑定失败,错误代码如下:" & getError & "，请联系" & Contact
        MsgBox "句柄" & setHwnd & "前台绑定失败,错误代码如下:" & getError & "，请联系" & Contact, 4096, "紫猫编程学院"
        ExitScript
    Else
        TracePrint "句柄" & setHwnd & "前台绑定成功"
    End If
End Sub
Sub zmBindWindows(setHwnd)//标准后台windows绑定
    Dim getError
    dm_ret = dm.BindWindow(setHwnd, "gdi2", "windows", "windows", 0)
    Delay 2000
    If dm_ret = 0 Then
        getError = dm.GetLastError()
        TracePrint "句柄" & setHwnd & "标准后台windows绑定失败,错误代码如下:" & getError & "，请联系" & Contact
        MsgBox "句柄" & setHwnd & "标准后台windows绑定失败,错误代码如下:" & getError & "，请联系" & Contact, 4096, "紫猫编程学院"
        ExitScript
    Else
        TracePrint "句柄" & setHwnd & "标准后台windows绑定成功"
    End If
End Sub
Sub zmBindDX(setHwnd)//标准后台DX绑定
    Dim getError
    dm_ret = dm.SetWindowState(setHwnd, 1)
    Delay 1000
    dm_ret = dm.BindWindow(setHwnd, "dx", "dx", "dx", 0)
    Delay 2000
    If dm_ret = 0 Then
        getError = dm.GetLastError()
        TracePrint "句柄" & setHwnd & "标准后台DX绑定失败,错误代码如下:" & getError & "，请联系" & Contact
        MsgBox "句柄" & setHwnd & "标准后台DX绑定失败,错误代码如下:" & getError & "，请联系" & Contact, 4096, "紫猫编程学院"
        ExitScript
    Else
        TracePrint "句柄" & setHwnd & "标准后台DX绑定成功"
    End If
End Sub
Sub zmLClick(x, y)//左键单击
    dm.MoveTo x, y
    Delay 100
    dm.LeftClick
End Sub
Sub zmRClick(x, y)//右键单击
    dm.MoveTo x, y
    Delay 100
    dm.RightClick
End Sub
Sub zmLDClick(x, y)//左键双击
    dm.MoveTo x, y
    Delay 100
    dm.LeftDoubleClick
End Sub
Sub zmLDown(x, y)//左键按下
    dm.MoveTo x, y
    Delay 100
    dm.LeftDown
End Sub
Sub zmLUp(x, y)//左键弹起
    dm.MoveTo x, y
    Delay 100
    dm.LeftUp
End Sub
Sub zmRDown(x, y)//右键按下
    dm.MoveTo x, y
    Delay 100
    dm.RightDown
End Sub
Sub zmRUp(x, y)//右键弹起
    dm.MoveTo x, y
    Delay 100
    dm.RightUp
End Sub
Sub zmKPress(setKey)//按键
    If VarType(setKey) = 8 Then
        dm.KeyPressChar setKey
    Else
        dm.KeyPress setKey
    End If
End Sub
Sub zmKDown(setKey)//按键按住
    If VarType(setKey) = 8 Then
        dm.KeyDownChar setKey
    Else
        dm.KeyDown setKey
    End If
End Sub
Sub zmKUp(setKey)//按键弹起
    If VarType(setKey) = 8 Then
        dm.KeyUpChar setKey
    Else
        dm.KeyUp setKey
    End If
End Sub
Sub zmKPressStr(KeysGroup, yanchi)//通过模拟按键输入字符
    Dim KeyArr(48)
    KeyArr(0) = "a〓A〓65" : KeyArr(1) = "b〓B〓66" : KeyArr(2) = "c〓C〓67" : KeyArr(3) = "d〓D〓68" : KeyArr(4) = "e〓E〓69"
    KeyArr(5) = "f〓F〓70" : KeyArr(6) = "g〓G〓71" : KeyArr(7) = "h〓H〓72" : KeyArr(8) = "i〓I〓73" : KeyArr(9) = "j〓J〓74"
    KeyArr(10) = "k〓K〓75" : KeyArr(11) = "l〓L〓76" : KeyArr(12) = "m〓M〓77" : KeyArr(13) = "n〓N〓78" : KeyArr(14) = "o〓O〓79"
    KeyArr(15) = "p〓P〓80" : KeyArr(16) = "q〓Q〓81" : KeyArr(17) = "r〓R〓82" : KeyArr(18) = "s〓S〓83" : KeyArr(19) = "t〓T〓84"
    KeyArr(20) = "u〓U〓85" : KeyArr(21) = "v〓V〓86" : KeyArr(22) = "w〓W〓87" : KeyArr(23) = "x〓X〓88" : KeyArr(24) = "y〓Y〓89"
    KeyArr(25) = "z〓Z〓90" : KeyArr(26) = "`〓~〓192" : KeyArr(27) = "1〓!〓49" : KeyArr(28) = "2〓@〓50" : KeyArr(29) = "3〓#〓51"
    KeyArr(30) = "4〓$〓52" : KeyArr(31) = "5〓%〓53" : KeyArr(32) = "6〓^〓54" : KeyArr(33) = "7〓&〓55" : KeyArr(34) = "8〓*〓56"
    KeyArr(35) = "9〓(〓57" : KeyArr(36) = "0〓)〓48" : KeyArr(37) = "-〓_〓189" : KeyArr(38) = "=〓+〓187" : KeyArr(39) = "[〓{〓219"
    KeyArr(40) = "]〓}〓221" : KeyArr(41) = "\〓|〓220" : KeyArr(42) = ";〓:〓186" : KeyArr(43) = "'〓""〓222" : KeyArr(44) = ",〓<〓188"
    KeyArr(45) = ".〓>〓190" : KeyArr(46) = "/〓?〓191" : KeyArr(47) = " 〓 〓32" : KeyArr(48) = "·〓~〓192"
    Dim Num, i, m, n, MyKeyS, KeyS
    Num = Len(KeysGroup)
    For i = 1 To Num    
        KeyS = Mid(KeysGroup, i, 1)
        For n = 0 To 46
            MyKeyS = Split(KeyArr(n), "〓")
            If KeyS = MyKeyS(0) Then
                dm.KeyPress Clng(MyKeyS(2))
                Exit For
            ElseIf KeyS = MyKeyS(1) Then
                dm.KeyDown 16
                Delay 50
                dm.KeyPress Clng(MyKeyS(2))
                Delay 50
                dm.KeyUp 16
                Exit For
            End If
        Next
        Delay yanchi
    Next
End Sub
Function zmFindImg(setImg)
    Dim ImgID
    ImgID = dm.FindPic(0, 0, setFindX, setFindY, setImg, "101010", 0.9, 0, ImgX, ImgY)
    TracePrint "单次找图: 在范围(0, 0, " & setFindX & ", " & setFindY & ")内查找图片(" & setImg & ")的结果为: 图片序号=" & ImgID & ", 坐标=(" & ImgX & ", " & ImgY & ")"
    If AllDisplayDebug = 1 And ImgID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\FI-" & zmReplaceE(Replace(setImg, ".bmp", "") & "-" & Time & "-" & zmRandom(10, 99), "/\:|", "_") & ".bmp")
    End If
    zmFindImg = ImgID
End Function
Function zmFindImgEx(x1, y1, x2, y2, setImg)
    Dim ImgID
    ImgID = dm.FindPic(x1, y1, x2, y2, setImg, "101010", 0.9, 0, ImgX, ImgY)
    TracePrint "单次找图: 在范围(" & x1 & ", " & y1 & ", " & x2 & ", " & y2 & ")内查找图片(" & setImg & ")的结果为: 图片序号=" & ImgID & ", 坐标=(" & ImgX & ", " & ImgY & ")"
    If AllDisplayDebug = 1 And ImgID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\FIE-" & zmReplaceE(Replace(setImg, ".bmp", "") & "-" & Time & "-" & zmRandom(10, 99), "/\:|", "_") & ".bmp")
    End If
    zmFindImgEx = ImgID
End Function
Function zmWaitImg(setImg, setTime)
    Dim ImgID, i
    For i = 0 To 10 * setTime
        ImgID = dm.FindPic(0, 0, setFindX, setFindY, setImg, "101010", 0.9, 0, ImgX, ImgY)
        If ImgID > - 1  Then
            Exit For
        End If
        Delay 100
    Next
    TracePrint "循环找图: 耗时=" & i & ",在范围(0, 0, " & setFindX & ", " & setFindY & ")内查找图片" & setImg & "的结果为: 图片序号=" & ImgID & ", 坐标=(" & ImgX & ", " & ImgY & ")"
    If AllDisplayDebug = 1 And ImgID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\WI-" & zmReplaceE(Replace(setImg, ".bmp", "") & "-" & Time & "-" & zmRandom(10, 99), "/\:|", "_") & ".bmp")
    End If
    zmWaitImg = ImgID
End Function
Function zmWaitImgEx(x1, y1, x2, y2, setImg, setTime)
    Dim ImgID, i
    For i = 0 To 10 * setTime
        ImgID = dm.FindPic(x1, y1, x2, y2, setImg, "101010", 0.9, 0, ImgX, ImgY)
        If ImgID > - 1  Then
            Exit For
        End If
        Delay 100
    Next
    TracePrint "循环找图: 耗时=" & i & ",在范围(" & x1 & ", " & y1 & ", " & x2 & ", " & y2 & ")内查找图片" & setImg & "的结果为:图片序号=" & ImgID & ", 坐标=(" & ImgX & ", " & ImgY & ")"
    If AllDisplayDebug = 1 And ImgID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\WIE-" & zmReplaceE(Replace(setImg, ".bmp", "") & "-" & Time & "-" & zmRandom(10, 99), "/\:|", "_") & ".bmp")
    End If
    zmWaitImgEx = ImgID
End Function
Function zmFindStr(setStr, setColor)
    Dim StrID
    StrID = dm.FindStr(0, 0, setFindX, setFindY, setStr, setColor, 1.0, StrX, StrY)
    TracePrint "单次找字: 在范围(0, 0, " & setFindX & ", " & setFindY & ")内查找颜色为(" & setColor & "),文字(" & setStr & ")的结果为: 文字序号=" & StrID & ", 坐标=(" & StrX & ", " & StrY & ")"
    If AllDisplayDebug = 1 And StrID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\FS-" & zmReplaceE(setStr & "-" & Time & "-" & zmRandom(10, 99), "/\:|*?<>" & Chr(34), "_") & ".bmp")
    End If
    zmFindStr = StrID
End Function
Function zmFindStrEx(x1, y1, x2, y2, setStr, setColor)
    Dim StrID
    StrID = dm.FindStr(x1, y1, x2, y2, setStr, setColor, 1.0, StrX, StrY)
    TracePrint "单次找字: 在范围(" & x1 & ", " & y1 & ", " & x2 & ", " & y2 & ")内查找颜色为(" & setColor & "),文字(" & setStr & ")的结果为: 文字序号=" & StrID & ", 坐标=(" & StrX & ", " & StrY & ")"
    If AllDisplayDebug = 1 And StrID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\FSE-" & zmReplaceE(setStr & "-" & Time & "-" & zmRandom(10, 99), "/\:|*?<>" & Chr(34), "_") & ".bmp")
    End If
    zmFindStrEx = StrID
End Function
Function zmWaitStr(setStr, setColor, setTime)
    Dim StrID, i
    For i = 0 to 10 * setTime
        StrID = dm.FindStr(0, 0, setFindX, setFindY, setStr, setColor, 1.0, StrX, StrY)
        If StrID > - 1  Then
            Exit For
        End If
        Delay 100
    Next
    TracePrint "循环找字: 耗时=" & i & ",在范围(0, 0, " & setFindX & ", " & setFindY & ")内查找颜色为("&setColor&"),文字(" & setStr & ")的结果为: 文字序号=" & StrID & ", 坐标=(" & StrX & ", " & StrY & ")"
    If AllDisplayDebug = 1 And StrID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\WS-" & zmReplaceE(setStr & "-" & Time & "-" & zmRandom(10, 99), "/\:|*?<>" & Chr(34), "_") & ".bmp")
    End If
    zmWaitStr = StrID
End Function
Function zmWaitStrEx(x1, y1, x2, y2, setStr, setColor, setTime)
    Dim StrID, i
    For i = 0 to 10 * setTime
        StrID = dm.FindStr(x1, y1, x2, y2, setStr, setColor, 1.0, StrX, StrY)
        If StrID > - 1  Then
            Exit For
        End If
        Delay 100
    Next
    TracePrint "循环找字: 耗时=" & i & ",在范围(" & x1 & ", " & y1 & ", " & x2 & ", " & y2 & ")内查找颜色为("&setColor&"),文字(" & setStr & ")的结果为: 文字序号=" & StrID & ", 坐标=(" & StrX & ", " & StrY & ")"
    If AllDisplayDebug = 1 And StrID = - 1 Then
        dm_ret = dm.CapturePre("\Debug\WSE-" & zmReplaceE(setStr & "-" & Time & "-" & zmRandom(10, 99), "/\:|*?<>" & Chr(34), "_") & ".bmp")
    End If
    zmWaitStrEx = StrID
End Function
Function zmOcr(x1, y1, x2, y2, color_format)
    Dim OcrStr
    OcrStr = dm.Ocr(x1, y1, x2, y2, color_format, 1.0)
    TracePrint "识别文字: 在范围(" & x1 & ", " & y1 & ", " & x2 & ", " & y2 & ")内识别颜色为(" & color_format & ")的文字结果=(" & OcrStr & ")"
    zmOcr = OcrStr
End Function
Function zmReplaceE(String1, SearchString, ReplaceString)
    Dim i
    For i = 1 To Len(SearchString)
        String1 = Replace(String1, Mid(SearchString, i, 1), ReplaceString)
    Next
    zmReplaceE = String1
End Function
Function zmRandom(num1, num2)//随机数
    Randomize
    If num1 > num2 Then
        zmRandom = Int((num1 - num2 + 1) * rnd + num2)
    Else
        zmRandom = Int((num2 - num1 + 1) * rnd + num1)
    End If   
End Function
Sub OnThreadExit()
    dm_ret = dm.UnBindWindow()
End Sub
