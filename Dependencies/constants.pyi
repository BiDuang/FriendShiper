"""
本模块为预置模块

提供一些实用常量

推荐使用ChinesePinyin-CodeCompletionHelper插件进行补全 支持jb全家桶以及vscode

不要用代码修改这里常量的值！！！

切忌修改！切忌修改！！切忌修改！！！会导致某些插件异常！！！
"""

# 消息类型
消息类型_临时会话 = 141
消息类型_好友通常消息 = 166
消息类型_讨论组消息 = 83

# 消息子临时类型
消息类型_临时会话_群临时 = 0
消息类型_临时会话_讨论组临时 = 1
消息类型_临时会话_公众号 = 129
消息类型_临时会话_网页QQ咨询 = 201

# 事件类型
群事件_我被邀请加入群 = 1
群事件_某人加入了群 = 2
群事件_某人申请加群 = 3
群事件_群被解散 = 4
群事件_某人退出了群 = 5
群事件_某人被踢出群 = 6
群事件_某人被禁言 = 7
群事件_某人撤回事件 = 8
群事件_某人被取消管理 = 9
群事件_某人被赋予管理 = 10
群事件_开启全员禁言 = 11
群事件_关闭全员禁言 = 12
群事件_开启匿名聊天 = 13
群事件_关闭匿名聊天 = 14
群事件_开启坦白说 = 15
群事件_关闭坦白说 = 16
群事件_允许群临时会话 = 17
群事件_禁止群临时会话 = 18
群事件_允许发起新的群聊 = 19
群事件_禁止发起新的群聊 = 20
群事件_允许上传群文件 = 21
群事件_禁止上传群文件 = 22
群事件_允许上传相册 = 23
群事件_禁止上传相册 = 24
群事件_某人被邀请入群 = 25
群事件_展示成员群头衔 = 26
群事件_隐藏成员群头衔 = 27
群事件_某人被解除禁言 = 28
空间事件_与我相关 = 29
群事件_我被踢出 = 30
框架事件_登录成功 = 31
群事件_群名变更 = 32
群事件_系统提示 = 33
群事件_群头像事件 = 34
群事件_入场特效 = 35
群事件_修改群名片 = 36
群事件_群被转让 = 37
讨论组事件_讨论组名变更 = 200
讨论组事件_某人撤回事件 = 201
讨论组事件_某人被邀请入群 = 202
讨论组事件_某人退出了群 = 203
讨论组事件_某人被踢出群 = 204
好友事件_被好友删除 = 100
好友事件_签名变更 = 101
好友事件_昵称改变 = 102
好友事件_某人撤回事件 = 103
好友事件_有新好友 = 104
好友事件_好友请求 = 105
好友事件_对方同意了您的好友请求 = 106
好友事件_对方拒绝了您的好友请求 = 107
好友事件_资料卡点赞 = 108
好友事件_签名点赞 = 109
好友事件_签名回复 = 110
好友事件_个性标签点赞 = 111
好友事件_随心贴回复 = 112
好友事件_随心贴增添 = 113
好友事件_系统提示 = 114
好友事件_随心贴点赞 = 115
好友事件_匿名提问_被提问 = 116
好友事件_匿名提问_被点赞 = 117
好友事件_匿名提问_被回复 = 118
好友事件_输入状态 = 119
登录事件_电脑上线 = 200
登录事件_电脑下线 = 201
登录事件_移动设备上线 = 202
登录事件_移动设备下线 = 203
登录事件_PCQQ登录验证请求 = 204

# api权限
权限_输出日志 = 0
权限_发送好友消息 = 1
权限_发送群消息 = 2
权限_发送群临时消息 = 3
权限_添加好友 = 4
权限_添加群 = 5
权限_删除好友 = 6
权限_置屏蔽好友 = 7
权限_置特别关心好友 = 8
权限_发送好友xml消息 = 9
权限_发送群xml消息 = 10
权限_发送好友json消息 = 11
权限_发送群json消息 = 12
权限_上传好友图片 = 13
权限_上传群图片 = 14
权限_上传好友语音 = 15
权限_上传群语音 = 16
权限_上传头像 = 17
权限_设置群名片 = 18
权限_取昵称_从缓存 = 19
权限_强制取昵称 = 20
权限_获取skey = 21
权限_获取pskey = 22
权限_获取clientkey = 23
权限_取框架QQ = 24
权限_取好友列表 = 25
权限_取群列表 = 26
权限_取群成员列表 = 27
权限_设置管理员 = 28
权限_取管理层列表 = 29
权限_取群名片 = 30
权限_取个性签名 = 31
权限_修改昵称 = 32
权限_修改个性签名 = 33
权限_删除群成员 = 34
权限_禁言群成员 = 35
权限_退群 = 36
权限_解散群 = 37
权限_上传群头像 = 38
权限_全员禁言 = 39
权限_群权限_发起新的群聊 = 40
权限_群权限_发起临时会话 = 41
权限_群权限_上传文件 = 42
权限_群权限_上传相册 = 43
权限_群权限_邀请好友加群 = 44
权限_群权限_匿名聊天 = 45
权限_群权限_坦白说 = 46
权限_群权限_新成员查看历史消息 = 47
权限_群权限_邀请方式设置 = 48
权限_撤回消息_群聊 = 49
权限_撤回消息_私聊本身 = 50
权限_设置位置共享 = 51
权限_上报当前位置 = 52
权限_是否被禁言 = 53
权限_处理好友验证事件 = 54
权限_处理群验证事件 = 55
权限_查看转发聊天记录内容 = 56
权限_上传群文件 = 57
权限_创建群文件夹 = 58
权限_设置在线状态 = 59
权限_QQ点赞 = 60
权限_取图片下载地址 = 61
权限_查询好友信息 = 63
权限_查询群信息 = 64
权限_框架重启 = 65
权限_群文件转发至群 = 66
权限_群文件转发至好友 = 67
权限_好友文件转发至好友 = 68
权限_置群消息接收 = 69
权限_取群名称_从缓存 = 70
权限_发送免费礼物 = 71
权限_取好友在线状态 = 72
权限_取QQ钱包个人信息 = 73
权限_获取订单详情 = 74
权限_提交支付验证码 = 75
权限_分享音乐 = 77
权限_更改群聊消息内容 = 78
权限_更改私聊消息内容 = 79
权限_群聊口令红包 = 80
权限_群聊拼手气红包 = 81
权限_群聊普通红包 = 82
权限_群聊画图红包 = 83
权限_群聊语音红包 = 84
权限_群聊接龙红包 = 85
权限_群聊专属红包 = 86
权限_好友口令红包 = 87
权限_好友普通红包 = 88
权限_好友画图红包 = 89
权限_好友语音红包 = 90
权限_好友接龙红包 = 91
权限_重命名群文件夹 = 92
权限_删除群文件夹 = 93
权限_删除群文件 = 94
权限_保存文件到微云 = 95
权限_移动群文件 = 96
权限_取群文件列表 = 97
权限_设置专属头衔 = 98
权限_下线指定QQ = 99
权限_登录指定QQ = 100
权限_取群未领红包 = 101
权限_发送输入状态 = 102
权限_修改资料 = 103
权限_打好友电话 = 104
权限_取群文件下载地址 = 105
权限_头像双击_好友 = 106
权限_头像双击_群 = 107
权限_取群成员简略信息 = 108
权限_群聊置顶 = 109
权限_私聊置顶 = 110
权限_取加群链接 = 111
权限_设为精华 = 112
权限_群权限_设置群昵称规则 = 113
权限_群权限_设置群发言频率 = 114
权限_群权限_设置群查找方式 = 115
权限_邀请好友加群 = 116
权限_置群内消息通知 = 117
权限_修改群名称 = 118
权限_下线其他设备 = 119
权限_登录网页取ck = 120
权限_发送群公告 = 121
权限_取群成员信息 = 122
权限_发送邮件 = 123
权限_取钱包cookie = 124
权限_取群网页cookie = 125
权限_取手Q邮箱cookie = 126
权限_转账 = 127
权限_余额提现 = 128
权限_取收款链接 = 129
权限_取群小视频下载地址 = 130
权限_取私聊小视频下载地址 = 131
权限_上传小视频 = 132
权限_取群成员概况 = 133
权限_添加好友_取验证类型 = 134
权限_群聊打卡 = 135
权限_群聊签到 = 136
权限_置群聊备注 = 137
权限_红包转发 = 138
权限_发送数据包 = 139
权限_请求ssoseq = 140
权限_取sessionkey = 141
权限_获取bkn_gtk = 142
权限_置好友验证方式 = 143
权限_上传照片墙图片 = 144
权限_付款 = 145
权限_修改支付密码 = 146
权限_账号搜索 = 147
权限_添加群_取验证类型 = 148
权限_领取红包 = 149
权限_获取红包领取详情 = 150
权限_取好友文件下载地址 = 151
权限_删除群成员_批量 = 152
权限_取扩列资料 = 153
权限_取资料展示设置 = 157
权限_设置资料展示 = 158
权限_获取当前登录设备信息 = 159
权限_提取图片文字 = 160
权限_取消精华 = 161
权限_群权限_设置加群方式 = 162
权限_群权限_群幸运字符 = 163
权限_群权限_一起写 = 164
权限_取QQ空间cookie = 165
权限_修改指定QQ缓存密码 = 166
权限_处理群验证事件_风险号 = 167
权限_查询网址安全性 = 168
权限_消息合并转发至好友 = 169
权限_消息合并转发至群 = 170
权限_禁言群匿名 = 171
权限_领取私聊普通红包 = 172
权限_领取群聊专属红包 = 173
权限_发送讨论组消息 = 174
权限_发送讨论组json消息 = 175
权限_发送讨论组xml消息 = 176
权限_发送讨论组临时消息 = 177
权限_撤回消息_讨论组 = 178
权限_回复QQ咨询会话 = 179
权限_发送订阅号私聊消息 = 180
权限_取讨论组名称_从缓存 = 181
权限_修改讨论组名称 = 182
权限_取讨论组成员列表 = 183
权限_强制取自身匿名Id = 184
权限_取订阅号列表 = 185
权限_取讨论组列表 = 186
权限_邀请好友加群_批量 = 187
权限_邀请好友加入讨论组_批量 = 188
权限_讨论组口令红包 = 189
权限_讨论组拼手气红包 = 190
权限_讨论组普通红包 = 191
权限_讨论组画图红包 = 192
权限_讨论组语音红包 = 193
权限_讨论组接龙红包 = 194
权限_讨论组专属红包 = 195
权限_领取讨论组专属红包 = 196
权限_取讨论组未领红包 = 197
权限_取讨论组文件下载地址 = 198
权限_发送QQ咨询会话 = 199
权限_创建群聊 = 200
权限_取群应用列表 = 201
权限_退出讨论组 = 202
权限_群验证消息接收设置 = 203
权限_转让群 = 204
权限_修改好友备注 = 205
权限_删除讨论组成员 = 206
权限_讨论组文件转发至群 = 207
权限_讨论组文件转发至好友 = 208

# 信息框
信息框_用户单击_确认钮 = 0
信息框_用户单击_取消钮 = 1
信息框_用户单击_放弃钮 = 2
信息框_用户单击_重试钮 = 3
信息框_用户单击_忽略钮 = 4
信息框_用户单击_是钮 = 5
信息框_用户单击_否钮 = 6
信息框_属性_按钮_确认钮 = 0
信息框_属性_按钮_确认取消钮 = 1
信息框_属性_按钮_放弃重试忽略钮 = 2
信息框_属性_按钮_取消是否钮 = 3
信息框_属性_按钮_是否钮 = 4
信息框_属性_按钮_重试取消钮 = 5
信息框_属性_图标_错误图标 = 16
信息框_属性_图标_询问图标 = 32
信息框_属性_图标_警告图标 = 48
信息框_属性_图标_信息图标 = 64
信息框_属性_缺省_默认按钮一 = 0
信息框_属性_缺省_默认按钮二 = 256
信息框_属性_缺省_默认按钮三 = 512
信息框_属性_缺省_默认按钮四 = 768
信息框_属性_等待_程序等待 = 0
信息框_属性_等待_系统等待 = 4096
信息框_属性_其他_位于前台 = 65536
信息框_属性_其他_文本右对齐 = 524288

# 输入框
输入框_输入方式_输入文本 = 1
输入框_输入方式_输入整数 = 2
输入框_输入方式_输入小数 = 3
输入框_输入方式_输入密码 = 4
