"""
小栗子PythonRunner 开发模块

本模块声明了pyrunner所有函数

如有错误还请指正！！感激不尽！！！

如有可空参数，填写默认值即可（int:0  str:''  bool:False）
"""
from typing import Union


#api
def send_group_msg(框架QQ: int, 群号: int, 发送内容: str, 匿名发送: bool) -> str:
    """
    发送群消息

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 发送内容: 发送内容
    :param 匿名发送: 匿名发送
    """
    ...


def log(日志: str, 文字颜色: str, 背景颜色: str) -> str:
    """
    输出日志

    :param 日志: 日志
    :param 文字颜色: 文字颜色 #xxxxxx
    :param 背景颜色: 背景颜色 #xxxxxx
    """
    ...


def amr_encode(音频文件路径: str) -> bytearray:
    """
    amr编码

    无权限要求

    :param 音频文件路径: 音频文件路径 注意文件后缀必须和文件格式相对应
    """
    ...


def does_api_have_perm(权限: int) -> bool:
    """
    api是否有权限

    判断某api是否有权限

    :param 权限: 权限 constants.权限_
    """
    ...


def like(框架QQ: int, 对方QQ: int) -> str:
    """
    QQ点赞

    注意，非好友情况下进行点赞时返回成功，但不一定真正点上了，对方开启陌生人点赞时才能点上(手Q默认关闭陌生人点赞)

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def silk_encode(音频文件路径: str) -> bytearray:
    """
    silk编码

    无权限要求

    :param 音频文件路径: 音频文件路径 注意文件后缀必须和文件格式相对应
    """
    ...


def silk_decode(音频文件路径: str) -> bytearray:
    """
    silk解码

    无权限要求

    :param 音频文件路径: 音频文件路径 注意文件后缀必须和文件格式相对应
    """
    ...


def tea_encrypt(内容: bytearray, 秘钥: bytearray) -> bytearray:
    """
    TEA加密

    无权限限制

    :param 内容: 内容
    :param 秘钥: 秘钥
    """
    ...


def tea_decrypt(内容: bytearray, 秘钥: bytearray) -> bytearray:
    """
    TEA解密

    无权限限制

    :param 内容: 内容
    :param 秘钥: 秘钥
    """
    ...


def save_file_to_weiyun(框架QQ: int, 群号: int, 文件fileid: str) -> str:
    """
    保存文件到微云

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件fileid: 文件fileid
    """
    ...


def view_forward_content(框架QQ: int, resId: str) -> list[dict]:
    """
    查看转发聊天记录内容

    私聊消息也可以使用此命令解析，无权限时不执行

    返回群消息数据dict列表

    :param 框架QQ: 框架QQ
    :param resId: resId 可在xml消息代码中取到
    """
    ...


def query_friend_info(框架QQ: int, 对方QQ: int) -> Union[dict, bool]:
    """
    查询好友信息

    支持陌生人查询

    成功返回好友信息dict,失败返回false

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def query_group_info(框架QQ: int, 群号: int) -> Union[dict, bool]:
    """
    查询群信息

    成功返回群卡片信息dict,失败返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def check_url_security(框架QQ: int, 网址: str) -> int:
    """
    查询网址安全性

    403无权限,404框架QQ不存在,405框架QQ未登录,0正常访问,-1查询失败,1包含不安全内容,2非官方页面,3未知状态

    :param 框架QQ: 框架QQ
    :param 网址: 网址
    """
    ...


def withdraw_group_msg(框架QQ: int, 群号: int, 消息Random: int, 消息Req: int) -> bool:
    """
    撤回消息_群聊

    在群消息事件中使用，能收到并撤回自己发的消息，管理员可撤回其他人的，失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 消息Random: 消息Random
    :param 消息Req: 消息Req
    """
    ...


def withdraw_private_msg(框架QQ: int, 对方QQ: int, 消息Random: int, 消息Req: int, 消息接收时间: int) -> bool:
    """
    撤回消息_私聊本身

    用于撤回自己发的消息，其他设备的个人消息通知也可以撤回，也可以直接撤回私聊对象的消息

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 消息Random: 消息Random
    :param 消息Req: 消息Req
    :param 消息接收时间: 消息接收时间
    """
    ...


def withdraw_discussion_msg(框架QQ: int, 讨论组Id: int, 消息Random: int, 消息Req: int) -> bool:
    """
    撤回消息_讨论组

    失败或无权限返回false,讨论组只能撤回自身的消息,不能撤回其他人的消息

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号 data['from_group']
    :param 消息Random: 消息Random
    :param 消息Req: 消息Req
    """
    ...


def handle_friend_verification(框架QQ: int, 触发QQ: int, 消息Seq: int, 操作类型: int) -> int:
    """
    处理好友验证事件

    在好友验证事件下使用，无权限时不执行

    无返回值，固定返回0

    :param 框架QQ: 框架QQ
    :param 触发QQ: 触发QQ
    :param 消息Seq: 消息Seq
    :param 操作类型: 操作类型 1同意 2拒绝
    """
    ...


def handle_group_verification(框架QQ: int, 来源群号: int, 触发QQ: int, 消息Seq: int, 操作类型: int, 事件类型: int, 拒绝理由: str) -> int:
    """
    处理群验证事件

    在群验证事件下使用，无权限时不执行

    无返回值，固定返回0

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号
    :param 触发QQ: 触发QQ
    :param 消息Seq: 消息Seq
    :param 操作类型: 操作类型 11同意 12拒绝  14忽略
    :param 事件类型: 事件类型 #群事件_某人申请加群/#群事件_我被邀请加入群
    :param 拒绝理由: 拒绝理由 当拒绝时，可在此设置拒绝理由
    """
    ...


def handle_group_verification_risk_qq(框架QQ: int, 来源群号: int, 触发QQ: int, 消息Seq: int, 操作类型: int, 事件类型: int,
                                      拒绝理由: str) -> int:
    """
    处理群验证事件_风险号

    专门处理被过滤的加群申请,在群验证事件下使用,无权限时不执行

    无返回值，固定返回0

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号
    :param 触发QQ: 触发QQ
    :param 消息Seq: 消息Seq
    :param 操作类型: 操作类型 11同意 12拒绝  14忽略
    :param 事件类型: 事件类型 #群事件_某人申请加群
    :param 拒绝理由: 拒绝理由 当拒绝时,可在此设置拒绝理由
    """
    ...


def create_group(框架QQ: int, 邀请QQ: list[int], 来源群号: int) -> tuple[str, int]:
    """
    创建群聊

    返回(函数返回值, 新群群号)

    :param 框架QQ: 框架QQ
    :param 邀请QQ: 邀请QQ 数组, 多个邀请QQ
    :param 来源群号: 来源群号 若邀请QQ来源是群成员，则在此说明群号，否则留空，表明来源是好友
    """
    ...


def create_group_folder(框架QQ: int, 群号: int, 文件夹名: str) -> str:
    """
    创建群文件夹

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件夹名: 文件夹名
    """
    ...


def call_friend(框架QQ: int, 对方QQ: int) -> int:
    """
    打好友电话

    不建议频繁使用

    无返回值，固定返回0

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def log_in_webpage_get_ck(框架QQ: int, 回调跳转地址: str, appid: str, daid: str) -> Union[str, bool]:
    """
    登录网页取ck

    失败返回false

    :param 框架QQ: 框架QQ
    :param 回调跳转地址: 回调跳转地址 不能url编码！如QQ空间是：https://h5.qzone.qq.com/mqzone/index
    :param appid: appid 如QQ空间是：549000929
    :param daid: daid 如QQ空间是：5
    """
    ...


def login_designate_qq(框架QQ: int) -> bool:
    """
    登录指定QQ

    敏感权限，建议使用前检查是否有权限，返回true表示成功投递密码登录任务，不代表对应QQ登录成功

    :param 框架QQ: 框架QQ
    """
    ...


def send_consultation_session(框架QQ: int, 对方QQ: int, 消息内容: str) -> tuple[str, int, int]:
    """
    发送QQ咨询会话

    当对方开启了QQ咨询,则可通过QQ咨询主动向对方发送消息,若对方没有开启QQ咨询,则只能使用API【回复QQ咨询会话 send_consultation_reply】进行回复

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 消息内容: 消息内容
    """
    ...


def send_subscription_acc_msg(框架QQ: int, 订阅号Id: int, 消息内容: str) -> tuple[str, int, int]:
    """
    发送订阅号私聊消息

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 订阅号Id: 订阅号Id
    :param 消息内容: 消息内容
    """
    ...


def send_friend_json_msg(框架QQ: int, 好友QQ: int, json代码: str) -> tuple[str, int, int]:
    """
    发送好友json消息

    成功返回的time用于撤回消息

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 好友QQ: 好友QQ
    :param json代码: json代码
    """
    ...


def send_friend_xml_msg(框架QQ: int, 好友QQ: int, xml代码: str) -> tuple[str, int, int]:
    """
    发送好友xml消息

    成功返回的time用于撤回消息

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 好友QQ: 好友QQ
    :param xml代码: xml代码
    """
    ...


def send_friend_msg(框架QQ: int, 好友QQ: int, 发送内容: str) -> tuple[str, int, int]:
    """
    发送好友消息

    成功返回的time用于撤回消息

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 好友QQ: 好友QQ
    :param 发送内容: 发送内容
    """
    ...


def send_free_gift(框架QQ: int, 群号: int, 对方QQ: int, 礼物ID: int) -> str:
    """
    发送免费礼物

    绕过广告发送免费礼物

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ
    :param 礼物ID: 礼物ID 367告白话筒;299卡布奇诺;302猫咪手表;280牵你的手;281可爱猫咪;284神秘面具;285甜wink;286我超忙的;289快乐肥宅水;290幸运手链;313坚强;307绒绒手套; 312爱心口罩;308彩虹糖果
    """
    ...


def send_group_json_msg(框架QQ: int, 群号: int, json代码: str, 匿名发送: bool) -> str:
    """
    发送群json消息

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param json代码: json代码
    :param 匿名发送: 匿名发送
    """
    ...


def send_group_xml_msg(框架QQ: int, 群号: int, xml代码: str, 匿名发送: bool) -> str:
    """
    发送群xml消息

    若xml代码内存在html代码,需自己提前处理,不能在尾部附带链接等

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param xml代码: xml代码
    :param 匿名发送: 匿名发送
    """
    ...


def send_group_announcement(框架QQ: int, 群号: int, 标题: str, 内容: str, 图片: bytearray, 视频: str, 弹窗展示: bool, 需要确认: bool,
                            置顶: bool, 发送给新成员: bool, 引导修改群昵称: bool) -> str:
    """
    发送群公告

    http

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 标题: 标题 支持emoji表情,如：\uD83D\uDE01
    :param 内容: 内容 支持emoji表情,如：\uD83D\uDE01
    :param 图片: 图片 在公告当中插入图片,如果设置了[腾讯视频]参数,则不显示图片只显示视频
    :param 视频: 视频 公告当中插入视频,只支持腾讯视频,如：https://v.qq.com/x/cover/4gl2i78zd9idpi0/j0024zknymk.html
    :param 弹窗展示: 弹窗展示
    :param 需要确认: 需要确认
    :param 置顶: 置顶
    :param 发送给新成员: 发送给新成员
    :param 引导修改群昵称: 引导修改群昵称
    """
    ...


def send_group_tmp_msg(框架QQ: int, 群号: int, 对方QQ: int, 发送内容: str) -> tuple[str, int, int]:
    """
    发送群临时消息

    成功返回的time用于撤回消息

    返回(函数返回值, Random, Req)

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ
    :param 发送内容: 发送内容
    """
    ...


def send_input_stat(框架QQ: int, 对方QQ: int, 输入状态: int) -> bool:
    """
    发送输入状态

    在与他人私聊时，在发消息前使用，显得更有真实感

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 输入状态: 输入状态 1:正在输入,2:关闭显示,3:正在说话
    """
    ...


def send_data_packet(框架QQ: int, 包体序号: int, 最大等待时长: int, 数据: bytearray) -> Union[bytearray, bool]:
    """
    发送数据包

    向腾讯服务器发送数据包(完整的原始包),无权限等返回false,加密秘钥通过【取sessionkey get_session_key】API获取

    失败返回false

    :param 框架QQ: 框架QQ
    :param 包体序号: 包体序号 ssoseq,通过【请求ssoseq get_ssoseq】API获取
    :param 最大等待时长: 最大等待时长 毫秒,不填或小于0时不等待返回包,大于0时等待返回包
    :param 数据: 数据 返回数据参考传回,拉取返回包失败参考回空字节集
    """
    ...


def send_discussion_json_msg(框架QQ: int, 讨论组Id: int, Json代码: str) -> str:
    """
    发送讨论组json消息

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号 data['from_group']
    :param Json代码: Json代码
    """
    ...


def send_discussion_xml_msg(框架QQ: int, 讨论组Id: int, Xml代码: str) -> str:
    """
    发送讨论组xml消息

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号 data['from_group']
    :param Xml代码: Xml代码
    """
    ...


def send_discussion_temp_msg(框架QQ: int, 讨论组Id: int, 对方QQ: int, 消息内容: str) -> tuple[str, int, int]:
    """
    发送讨论组临时消息

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群聊数据.消息群号 data['from_group']
    :param 对方QQ: 对方QQ
    :param 消息内容: 消息内容
    """
    ...


def send_discussion_group_msg(框架QQ: int, 讨论组Id: int, 消息内容: str) -> str:
    """
    发送讨论组消息

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号 data['from_group']
    :param 消息内容: 消息内容 同群聊文本代码结构
    """
    ...


def send_email(框架QQ: int, 邮箱地址: str, 邮件标题: str, 邮件内容: str) -> str:
    """
    发送邮件

    邮件内容支持html，未处理需要验证码的情况，验证码的验证可以自己通过代码实现

    :param 框架QQ: 框架QQ
    :param 邮箱地址: 邮箱地址
    :param 邮件标题: 邮件标题
    :param 邮件内容: 邮件内容 支持html
    """
    ...


def share_music(框架QQ: int, 分享对象: int, 歌曲名: str, 歌手名: str, 跳转地址: str, 封面地址: str, 文件地址: str, 应用类型: int,
                分享类型: int) -> bool:
    """
    分享音乐

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 分享对象: 分享对象 分享的群或分享的好友QQ
    :param 歌曲名: 歌曲名
    :param 歌手名: 歌手名
    :param 跳转地址: 跳转地址 点击音乐json后跳转的地址
    :param 封面地址: 封面地址 音乐的封面图片地址
    :param 文件地址: 文件地址 音乐源文件地址，如https://xxx.com/xxx.mp3(VIP歌曲可省略)
    :param 应用类型: 应用类型 0QQ音乐 1虾米音乐 2酷我音乐 3酷狗音乐 4网易云音乐
    :param 分享类型: 分享类型 0私聊 1群聊
    """
    ...


def pay(框架QQ: int, QrcodeUrl: str, 银行卡序列: int, 支付密码: str) -> tuple[str, dict]:
    """
    付款

    扫描QQ钱包支付二维码来付款(购买QB,游戏道具等),成功返回json retcode=0 ,失败或无权限返回其他值

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param QrcodeUrl: QrcodeUrl QQ钱包支付二维码内容(需要自己识别二维码,将识别结果填入)
    :param 银行卡序列: 银行卡序列 大于0则表示使用银行卡支付反之用余额支付
    :param 支付密码: 支付密码
    """
    ...


def send_friend_drawing_red_packet(框架QQ: int, 总数量: int, 总金额: int, 对方QQ: int, 题目名: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    好友画图红包

    不支持非好友！

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 对方QQ: 对方QQ
    :param 题目名: 题目名 只能填手Q有的，如：庄周
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_friend_solitaire_red_packet(框架QQ: int, 总数量: int, 总金额: int, 对方QQ: int, 接龙内容: str, 支付密码: str, 银行卡序列: int) -> \
        tuple[str, dict]:
    """
    好友接龙红包

    不支持非好友！

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 对方QQ: 对方QQ
    :param 接龙内容: 接龙内容 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_friend_word_red_packet(框架QQ: int, 总数量: int, 总金额: int, 对方QQ: int, 口令: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    好友口令红包

    不支持非好友！

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 对方QQ: 对方QQ
    :param 口令: 口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_friend_red_packet(框架QQ: int, 总数量: int, 总金额: int, 对方QQ: int, 祝福语: str, 红包皮肤Id: int, 支付密码: str,
                           银行卡序列: int) -> tuple[str, dict]:
    """
    好友普通红包

    不支持非好友！

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 对方QQ: 对方QQ
    :param 祝福语: 祝福语 支持emoji
    :param 红包皮肤Id: 红包皮肤Id 1522光与夜之恋,1527代号:三国(打了一辈子仗),1525街霸:对决,1518代号:三国(俺送红包来了),1476天涯明月刀,1512一人之下。其他皮肤id自己找
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def forward_friend_file_to_friend(框架QQ: int, 目标QQ: int, fileId: str, filename: str, filesize: int) -> tuple[
    str, int, int, int]:
    """
    好友文件转发至好友

    失败或无权限返回false

    返回(函数返回值, Req, Random, time)

    :param 框架QQ: 框架QQ
    :param 目标QQ: 目标QQ
    :param fileId: fileId
    :param filename: filename
    :param filesize: filesize 文件大小
    """
    ...


def send_friend_voice_red_packet(框架QQ: int, 总数量: int, 总金额: int, 对方QQ: int, 语音口令: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    好友语音红包

    不支持非好友！

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 对方QQ: 对方QQ
    :param 语音口令: 语音口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def red_packet_msgno_calculate(目标QQ: int) -> str:
    """
    红包msgno计算

    无权限限制

    :param 目标QQ: 目标QQ
    """
    ...


def red_packet_data_encrypt(str: str, random: int) -> str:
    """
    红包数据加密

    无权限限制

    DES ECB No Padding

    :param str: str
    :param random: random
    """
    ...


def red_packet_data_decrypt(str: str, random: int) -> str:
    """
    红包数据解密

    无权限限制

    DES ECB No Padding

    :param str: str
    :param random: random
    """
    ...


def forward_red_packet(框架QQ: int, 红包ID: str, 目标对象: int, Type: int) -> str:
    """
    红包转发

    转发自己的红包到其他群或好友或讨论组

    :param 框架QQ: 框架QQ
    :param 红包ID: 红包ID
    :param 目标对象: 目标对象 以Type类型为准,如果是1则判断为QQ号2则判断为群号3则判断为讨论组号
    :param Type: Type 1为好友,2为群,3为讨论组
    """
    ...


def send_consultation_reply(框架QQ: int, 对方QQ: int, 会话Token: bytearray, 消息内容: str) -> tuple[str, int, int]:
    """
    回复QQ咨询会话

    当对方通过QQ咨询联系你,但是对方未开启QQ咨询时,只能通过此API进行回复

    返回(函数返回值, 消息Random, 消息Req)

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 会话Token: 会话Token 私聊消息数据.会话token,具有时效性,是对方推送的
    :param 消息内容: 消息内容
    """
    ...


def get_bkn_gtk(框架QQ: int, 自定义bkn_gtk: str) -> str:
    """
    获取bkn_gtk

    返回网页用到的bkn或者gtk,也可以自定义计算的值

    :param 框架QQ: 框架QQ
    :param 自定义bkn_gtk: 自定义bkn_gtk 如果此参数不为空值则提交自定义值,否则框架返回内部值
    """
    ...


def get_client_key(框架QQ: int) -> str:
    """
    获取clientkey

    成功返回clientkey

    :param 框架QQ: 框架QQ
    """
    ...


def get_pskey(框架QQ: int, 域: str) -> str:
    """
    获取pskey

    成功返回pskey

    :param 框架QQ: 框架QQ
    :param 域: 域 tenpay.com;openmobile.qq.com;docs.qq.com;connect.qq.com;qzone.qq.com;vip.qq.com;gamecenter.qq.com;qun.qq.com;game.qq.com;qqweb.qq.com;ti.qq.com;office.qq.com;mail.qq.com;mma.qq.com
    """
    ...


def get_skey(框架QQ: int) -> str:
    """
    获取skey

    成功返回skey

    :param 框架QQ: 框架QQ
    """
    ...


def get_current_login_device_info(框架QQ: int) -> tuple[str, dict]:
    """
    获取当前登录设备信息

    有权限限制

    返回(函数返回值, 登录设备信息dict)

    :param 框架QQ: 框架QQ
    """
    ...


def get_order_detail(框架QQ: int, 订单号: str) -> tuple[str, dict]:
    """
    获取订单详情

    通过此API可以查询QQ转账详情，查询人只能是转账方或接收方，当转账未能被接收人成功接收时，只能由转账方进行查询

    返回(函数返回值, 订单详情dict)

    :param 框架QQ: 框架QQ
    :param 订单号: 订单号 或者称之为transid
    """
    ...


def get_red_packet_receive_detail(框架QQ: int, 来源群号: int, 红包文本代码: str, 红包类型: int) -> str:
    """
    获取红包领取详情

    只有领取过该红包才能成功查询,返回腾讯原始json数据

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号 红包为好友红包时,此参数可以省略,为讨论组时此处为讨论组Id
    :param 红包文本代码: 红包文本代码
    :param 红包类型: 红包类型 1:好友,2:群,3:讨论组,其他:群临时
    """
    ...


def load_webpage(网址: str) -> bool:
    """
    加载网页

    调用框架内置浏览器加载显示指定网页,无权限限制

    :param 网址: 网址 支持本地文件路径(中文请url编码)
    """
    ...


def disband_group(框架QQ: int, 群号: int) -> bool:
    """
    解散群

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def mute_group_member(框架QQ: int, 群号: int, 群成员QQ: int, 禁言时长: int) -> bool:
    """
    禁言群成员

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ
    :param 禁言时长: 禁言时长 单位：秒，为0时解除禁言
    """
    ...


def mute_group_anonymous(框架QQ: int, 群号: int, 匿名昵称: str, 匿名标识: bytearray, 禁言时长: int) -> bool:
    """
    禁言群匿名

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 匿名昵称: 匿名昵称 可通过群聊消息数据获得
    :param 匿名标识: 匿名标识 可通过群聊消息数据获得,同一个匿名每条消息发送时的标识都不同
    :param 禁言时长: 禁言时长 单位s
    """
    ...


def is_framework_single_qq() -> bool:
    """
    框架是否为单Q

    判断框架是否为单Q版,无权限限制

    """
    ...


def receive_group_exclusive_red_packet(框架QQ: int, 来源群号: int, 来源QQ: int, 红包文本代码: str) -> str:
    """
    领取群聊专属红包

    仅仅支持群聊下的专属红包(当然指的是给自己的专属红包)

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号 红包来源群号
    :param 来源QQ: 来源QQ 红包发送者QQ
    :param 红包文本代码: 红包文本代码 红包消息的文本代码
    """
    ...


def receive_private_red_packet(框架QQ: int, 来源QQ: int, 红包文本代码: str, 类型: int) -> str:
    """
    领取私聊普通红包

    仅仅支持好友、群临时，仅限于普通红包

    :param 框架QQ: 框架QQ
    :param 来源QQ: 来源QQ 红包发送者QQ
    :param 红包文本代码: 红包文本代码 红包消息的文本代码
    :param 类型: 类型 0好友红包,1群临时红包
    """
    ...


def receive_discussion_red_packet(框架QQ: int, 来源讨论组Id: int, 来源QQ: int, 红包文本代码: str) -> str:
    """
    领取讨论组专属红包

    仅仅支持讨论组下的专属红包(当然指的是给自己的专属红包)

    :param 框架QQ: 框架QQ
    :param 来源讨论组Id: 来源讨论组Id 红包来源讨论组Id
    :param 来源QQ: 来源QQ 红包发送者QQ
    :param 红包文本代码: 红包文本代码 红包消息的文本代码
    """
    ...


def get_nick_constraint(框架QQ: int, 对方QQ: str) -> str:
    """
    强制取昵称

    成功返回昵称

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def get_anonymous_id_constraint(框架QQ: int, 群号: int) -> int:
    """
    强制取自身匿名Id

    失败或无权限返回0,禁止在其他设备更换匿名,否则匿名相关功能无效

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_ssoseq(框架QQ: int) -> int:
    """
    请求ssoseq

    无权限等返回0

    :param 框架QQ: 框架QQ
    """
    ...


def get_qq_space_cookie(框架QQ: int) -> str:
    """
    取QQ空间cookie

    敏感API,框架会自动刷新

    :param 框架QQ: 框架QQ
    """
    ...


def get_qq_wallet_info(框架QQ: int) -> tuple[str, dict]:
    """
    取QQ钱包个人信息

    包括余额、名字、银行卡等

    返回(函数返回值, QQ钱包信息dict)

    :param 框架QQ: 框架QQ
    """
    ...


def get_session_key(框架QQ: int) -> str:
    """
    取sessionkey

    成功返回16进制秘钥,敏感权限

    :param 框架QQ: 框架QQ
    """
    ...


def get_subscription_acc_list(框架QQ: int) -> list[dict]:
    """
    取订阅号列表

    返回订阅号信息dict列表

    :param 框架QQ: 框架QQ
    """
    ...


def get_signature(框架QQ: int, 对方QQ: int) -> str:
    """
    取个性签名

    成功返回个性签名

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ 可以填框架QQ本身
    """
    ...


def get_administrator_list(框架QQ: int, 群号: int) -> str:
    """
    取管理层列表

    仅针对群聊,讨论组有其他Api,第一行是群主，剩下的是管理员

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_friend_list(框架QQ: int) -> list[dict]:
    """
    取好友列表

    返回好友信息dict列表

    :param 框架QQ: 框架QQ
    """
    ...


def get_friend_file_download_link(框架QQ: int, FileId: str, FileName: str) -> str:
    """
    取好友文件下载地址

    支持好友、群临时、讨论组临时,获取好友分享的文件的下载地址(此方法只能用于好友文件获取下载链接,如果是群请调用<取群文件下载地址>)

    :param 框架QQ: 框架QQ
    :param FileId: FileId 该文件的ID
    :param FileName: FileName 该文件的文件名
    """
    ...


def get_friend_online_stat(框架QQ: int, 对方QQ: int) -> str:
    """
    取好友在线状态

    失败或无权限返回空，支持查询陌生人

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def get_group_join_link(框架QQ: int, 群号: int) -> str:
    """
    取加群链接

    不支持讨论组,失败返回空

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_card_msg_code(卡片消息文本代码: str) -> str:
    """
    取卡片消息代码

    无权限限制,传入卡片消息文本代码,返回卡片消息代码

    :param 卡片消息文本代码: 卡片消息文本代码 如: [customNode,key=xx,val=xx]
    """
    ...


def get_all_qq() -> str:
    """
    取框架QQ

    返回的数据是json格式,自行进行解析
    """
    ...


def get_framework_version() -> str:
    """
    取框架版本

    无权限限制
    """
    ...


def get_framework_expiration_time() -> str:
    """
    取框架到期时间

    无权限限制,返回示例：2025/1/1 00:00:00,年月日无补零,时分秒有补零
    """
    ...


def get_data_folder() -> str:
    """
    取插件数据目录

    返回绝对plugins\data\路径，以\结尾
    """
    ...


def get_making_friends_profile(框架QQ: int, 对方QQ: int) -> str:
    """
    取扩列资料

    取对方的扩列资料,即使对方隐藏也可以查询

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def get_nick_cache(对方QQ: str) -> str:
    """
    取昵称_从缓存

    成功返回昵称

    :param 对方QQ: 对方QQ
    """
    ...


def get_wallet_cookie(框架QQ: int) -> str:
    """
    取钱包cookie

    敏感API,框架会自动刷新

    :param 框架QQ: 框架QQ
    """
    ...


def get_group_member_profile(框架QQ: int, 群号: int) -> str:
    """
    取群成员概况

    成功返回json,含有群上限、群人数、群成员统计概况

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_group_member_info_brief(框架QQ: int, 群号: int) -> tuple[str, dict]:
    """
    取群成员简略信息

    http，可取群上限、群主、管理员

    返回(函数返回值, 群成员状况简略信息dict)

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_group_member_list(框架QQ: int, 群号: int) -> list[dict]:
    """
    取群成员列表

    返回群成员信息dict列表

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_group_member_info(框架QQ: int, 群号: int, 对方QQ: int) -> tuple[str, dict]:
    """
    取群成员信息

    获取一个群成员的相关信息

    返回(函数返回值, 群成员信息V2)

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ
    """
    ...


def get_group_list(框架QQ: int) -> list[dict]:
    """
    取群列表

    返回群信息dict列表

    :param 框架QQ: 框架QQ
    """
    ...


def get_group_name_cache(群号: str) -> str:
    """
    取群名称_从缓存

    成功返回群名称，如果是框架QQ没加的群，请使用[查询群信息]，查询后也会记录缓存

    :param 群号: 群号
    """
    ...


def get_group_member_card(框架QQ: int, 群号: int, 群成员QQ: int) -> str:
    """
    取群名片

    成功返回群名片，注意，如果群成员的群名片未设置或群名片为空白，返回结果均为空

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ
    """
    ...


def get_group_webpage_cookie(框架QQ: int) -> str:
    """
    取群网页cookie

    敏感API,框架会自动刷新

    :param 框架QQ: 框架QQ
    """
    ...


def get_group_not_receive_red_package_info(框架QQ: int, 群号: int) -> list[dict]:
    """
    取群未领红包

    注意：使用此API获取的红包只能用手Q上"群未领红包"入口的http请求领取

    返回群未领红包数据dict列表

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_group_file_list(框架QQ: int, 群号: int, 文件夹名: str, 数据: int) -> tuple[str, list[dict]]:
    """
    取群文件列表

    返回(函数返回值, 群文件信息dict列表)

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件夹名: 文件夹名 欲查看的文件夹名，根目录留空或填/
    :param 数据: 数据 参考 数组,
    """
    ...


def get_group_file_download_link(框架QQ: int, 来源群号: int, 文件id: str, 文件名: str) -> str:
    """
    取群文件下载地址

    文件下载地址在返回的json里面，具有时效性，请及时下载

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号 QQ必须在群内
    :param 文件id: 文件id
    :param 文件名: 文件名 可自定义，必须带文件类型后缀，如xxx.zip
    """
    ...


def get_group_short_video_download_link(框架QQ: int, 来源群号: int, 来源QQ: int, param: str, hash1: str, 文件名: str) -> str:
    """
    取群小视频下载地址

    支持讨论组,成功返回json含下载链接

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号
    :param 来源QQ: 来源QQ
    :param param: param 可通过文本代码获取
    :param hash1: hash1 可通过文本代码获取
    :param 文件名: 文件名 xxx.mp4,必须带上文件后缀
    """
    ...


def get_group_application_list(框架QQ: int, 群号: int) -> list[dict]:
    """
    取群应用列表

    成功返回群应用数量

    返回群应用信息dict列表

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def get_payment_link(框架QQ: int, 收款金额: int, 说明文本: str) -> str:
    """
    取收款链接

    返回收款链接,可借此生成收款二维码

    :param 框架QQ: 框架QQ
    :param 收款金额: 收款金额 指定收款金额,单位：分
    :param 说明文本: 说明文本 备注
    """
    ...


def get_mailbox_cookie(框架QQ: int) -> str:
    """
    取手Q邮箱cookie

    敏感API,框架会自动刷新,邮箱sid在cookie当中,键名为xxsid

    :param 框架QQ: 框架QQ
    """
    ...


def get_private_short_video_download_link(框架QQ: int, 来源QQ: int, param: str, hash1: str, 文件名: str) -> str:
    """
    取私聊小视频下载地址

    成功返回json含下载链接

    :param 框架QQ: 框架QQ
    :param 来源QQ: 来源QQ
    :param param: param 可通过文本代码获取
    :param hash1: hash1 可通过文本代码获取
    :param 文件名: 文件名 xxx.mp4,必须带上文件后缀
    """
    ...


def get_discussion_member_list(框架QQ: int, 讨论组Id: int) -> list[dict]:
    """
    取讨论组成员列表

    传回数据的第一个QQ账号是讨论组的拥有者

    返回讨论组成员信息dict列表

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号
    """
    ...


def get_discussion_list(框架QQ: int) -> list[dict]:
    """
    取讨论组列表

    返回讨论组信息dict列表

    :param 框架QQ: 框架QQ
    """
    ...


def get_discussion_name_cache(讨论组Id: str) -> str:
    """
    取讨论组名称_从缓存

    失败或无权限返回空,从缓存取讨论组名(当取出为空时,先使用【取讨论组成员列表 get_discussion_member_list】,之后缓存内便有讨论组的名称)

    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号
    """
    ...


def get_discussion_not_receive_red_package_info(框架QQ: int, 讨论组Id: int) -> list[dict]:
    """
    取讨论组未领红包

    注意：使用此API获取的红包只能用手Q上"讨论组未领红包"入口的http请求领取

    返回群未领红包数据dict列表

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id
    """
    ...


def get_discussion_file_download_link(框架QQ: int, 讨论组Id: int, 文件id: str, 文件名: str) -> str:
    """
    取讨论组文件下载地址

    文件下载地址在返回的json里面，具有时效性，请及时下载

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id QQ必须在讨论组内
    :param 文件id: 文件id
    :param 文件名: 文件名 可自定义，必须带文件类型后缀，如xxx.zip
    """
    ...


def get_pic_download_link(图片代码: str, 框架QQ: int, 群号: int) -> str:
    """
    取图片下载地址

    支持群聊、私聊、讨论组、闪照、秀图

    :param 图片代码: 图片代码 支持群聊、私聊、讨论组的图片、闪照代码，注意是图片代码
    :param 框架QQ: 框架QQ 群聊图片必填，私聊图片必空
    :param 群号: 群号 群聊图片必填，私聊图片必空
    """
    ...


def cancel_essence(框架QQ: int, 群号: int, 消息Req: int, 消息Random: int) -> bool:
    """
    取消精华

    取消某条精华群消息,成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 消息Req: 消息Req
    :param 消息Random: 消息Random
    """
    ...


def get_info_display_setting(框架QQ: int, 对方QQ: int) -> tuple[str, dict]:
    """
    取资料展示设置

    支持查询他人的设置

    返回(函数返回值, 资料展示设置数据dict)

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def mute_group_all(框架QQ: int, 群号: int, 是否开启: bool) -> bool:
    """
    全员禁言

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否开启: 是否开启
    """
    ...


def group_check_in(框架QQ: int, 群号: int) -> str:
    """
    群聊打卡

    返回json

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def send_group_drawing_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 题目名: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    群聊画图红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 题目名: 题目名 只能填手Q有的，如：庄周
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_group_solitaire_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 接龙内容: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    群聊接龙红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 接龙内容: 接龙内容 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_group_word_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 口令: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    群聊口令红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 口令: 口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_group_random_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 祝福语: str, 红包皮肤Id: int, 支付密码: str,
                                 银行卡序列: int) -> tuple[str, dict]:
    """
    群聊拼手气红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 祝福语: 祝福语 支持emoji
    :param 红包皮肤Id: 红包皮肤Id 1522光与夜之恋,1527代号:三国(打了一辈子仗),1525街霸:对决,1518代号:三国(俺送红包来了),1476天涯明月刀,1512一人之下。其他皮肤id自己找
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_group_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 祝福语: str, 红包皮肤Id: int, 支付密码: str, 银行卡序列: int) -> \
        tuple[str, dict]:
    """
    群聊普通红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 祝福语: 祝福语 支持emoji
    :param 红包皮肤Id: 红包皮肤Id 1522光与夜之恋,1527代号:三国(打了一辈子仗),1525街霸:对决,1518代号:三国(俺送红包来了),1476天涯明月刀,1512一人之下。其他皮肤id自己找
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def group_sign_in(框架QQ: int, 群号: int, 附加参数: str) -> bool:
    """
    群聊签到

    成功返回true,失败或无权限返回false,传入附加参数自定义签到内容(附加参数可抓旧版QQhttp数据获得)

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 附加参数: 附加参数 签到数据,如:template_data=&gallery_info=%7B%22category_id%22%3A9%2C%22page%22%3A0%2C%22pic_id%22%3A124%7D&template_id=%7B%7D&client=2&lgt=0&lat=0&poi=&pic_id=&text=%E5%AD%A6%E4%B9%A0%E6%89%93%E5%8D%A1
    """
    ...


def send_group_voice_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 语音口令: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    群聊语音红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 语音口令: 语音口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def pin_group(框架QQ: int, 群号: int, 置顶: bool) -> bool:
    """
    群聊置顶

    成功返回true，失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 置顶: 置顶 是否置顶
    """
    ...


def send_group_exclusive_red_packet(框架QQ: int, 总数量: int, 总金额: int, 群号: int, 领取人: str, 祝福语: str, 是否均分: bool, 支付密码: str,
                                    银行卡序列: int) -> tuple[str, dict]:
    """
    群聊专属红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 群号: 群号
    :param 领取人: 领取人 多个领取人QQ用|分隔
    :param 祝福语: 祝福语 支持emoji
    :param 是否均分: 是否均分 均分时每个领取人领取金额相同
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def group_perm_initiate_temp_session(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_发起临时会话

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_create_new_group(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_发起新的群聊

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_anonymous(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_匿名聊天

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_lucky_characters(框架QQ: int, 群号: int, 是否开启: bool) -> bool:
    """
    群权限_群幸运字符

    失败或无权限或非管理员返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否开启: 是否开启
    """
    ...


def group_perm_upload_files(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_上传文件

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_upload_album(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_上传相册

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_set_add_method(框架QQ: int, 群号: int, 加群方式: int, 问题: str, 答案: str) -> bool:
    """
    群权限_设置加群方式

    失败或无权限或非管理员返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 加群方式: 加群方式 0允许任何人 1需要发送验证消息 2需要回答问题并由管理员审核 3需要正确回答问题 4不允许任何人加群
    :param 问题: 问题 方式为2、3时必填
    :param 答案: 答案 方式为3时必填
    """
    ...


def group_perm_set_search_method(框架QQ: int, 群号: int, 查找方式: int) -> bool:
    """
    群权限_设置群查找方式

    成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 查找方式: 查找方式 0不允许,1通过群号或关键词,2仅可通过群号
    """
    ...


def group_perm_set_speak_frequency(框架QQ: int, 群号: int, 限制条数: int) -> bool:
    """
    群权限_设置群发言频率

    成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 限制条数: 限制条数 限制每分钟多少条发言,为0表示无限制
    """
    ...


def group_perm_set_nick_rule(框架QQ: int, 群号: int, 名片规则: str) -> bool:
    """
    群权限_设置群昵称规则

    成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 名片规则: 名片规则 对于易语言不支持的utf8字符,需usc2编码
    """
    ...


def group_perm_to_be_honest(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_坦白说

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_new_member_view_history_msg(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_新成员查看历史消息

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_set_invite_mode(框架QQ: int, 群号: int, 方式: int) -> bool:
    """
    群权限_邀请方式设置

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 方式: 方式 1 无需审核;2 需要管理员审核;3 100人以内无需审核
    """
    ...


def group_perm_invite_friends(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_邀请好友加群

    设置群聊权限,机器人必须是管理员或群主,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def group_perm_write_together(框架QQ: int, 群号: int, 是否允许: bool) -> bool:
    """
    群权限_一起写

    失败或无权限或非管理员返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否允许: 是否允许
    """
    ...


def forward_group_file_to_friend(框架QQ: int, 来源群号: int, 目标QQ: int, fileId: str, filename: str, filesize: int) -> Union[
    tuple[int, int, int], bool]:
    """
    群文件转发至好友

    失败或无权限返回false 成功返回(Req, Random, time)

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号
    :param 目标QQ: 目标QQ
    :param fileId: fileId
    :param filename: filename
    :param filesize: filesize 文件大小
    """
    ...


def forward_group_file_to_group(框架QQ: int, 来源群号: int, 目标群号: int, fileId: str) -> bool:
    """
    群文件转发至群

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 来源群号: 来源群号
    :param 目标群号: 目标群号
    :param fileId: fileId
    """
    ...


def set_group_verify_msg_receive(框架QQ: int, 群号: int, 对方QQ: int, 接收验证消息: bool) -> bool:
    """
    群验证消息接收设置

    设置指定管理员是否接收群验证消息,失败或无权限返回false,需要机器人为群主,否则无法设置

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ 管理员QQ
    :param 接收验证消息: 接收验证消息
    """
    ...


def delete_friend(框架QQ: int, 对方QQ: int) -> str:
    """
    删除好友

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def delete_group_member(框架QQ: int, 群号: int, 群成员QQ: int, 拒绝加群申请: bool) -> bool:
    """
    删除群成员

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ
    :param 拒绝加群申请: 拒绝加群申请
    """
    ...


def delete_group_members(框架QQ: int, 群号: int, 群成员QQ: list[int], 拒绝加群申请: bool) -> bool:
    """
    删除群成员_批量

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ 数组,
    :param 拒绝加群申请: 拒绝加群申请
    """
    ...


def delete_group_file(框架QQ: int, 群号: int, 文件fileid: str, 文件夹名: str) -> str:
    """
    删除群文件

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件fileid: 文件fileid
    :param 文件夹名: 文件夹名 文件所在的文件夹名，根目录留空或填/
    """
    ...


def delete_group_folder(框架QQ: int, 群号: int, 文件夹名: str) -> str:
    """
    删除群文件夹

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件夹名: 文件夹名
    """
    ...


def delete_discussion_member(框架QQ: int, 讨论组Id: int, 对方QQ: int) -> bool:
    """
    删除讨论组成员

    失败或无权限返回false,需要机器人为讨论组拥有者,否则没有权重

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id
    :param 对方QQ: 对方QQ
    """
    ...


def upload_location(框架QQ: int, 群号: int, 经度: int, 纬度: int) -> bool:
    """
    上报当前位置

    大约3s上报一次，不得过快，失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 经度: 经度 如：121.711540
    :param 纬度: 纬度 如：31.403343
    """
    ...


def upload_friend_picture(框架QQ: int, 好友QQ: int, 是否闪照: bool, pic: bytearray, 宽度: int, 高度: int, 动图: bool) -> str:
    """
    上传好友图片

    成功返回图片代码

    :param 框架QQ: 框架QQ
    :param 好友QQ: 好友QQ
    :param 是否闪照: 是否闪照 是否设置为闪照
    :param pic: pic
    :param 宽度: 宽度
    :param 高度: 高度
    :param 动图: 动图 为真时可自动播放动图
    """
    ...


def upload_friend_voice(框架QQ: int, 好友QQ: int, 语音类型: int, 语音文字: str, audio: bytearray, 时长: int) -> str:
    """
    上传好友语音

    成功返回语音代码

    :param 框架QQ: 框架QQ
    :param 好友QQ: 好友QQ
    :param 语音类型: 语音类型 0普通语音,1变声语音,2文字语音,3红包匹配语音
    :param 语音文字: 语音文字 文字语音填附加文字(腾讯貌似会自动替换为语音对应的文本),匹配语音填a、b、s、ss、sss，注意是小写
    :param audio: audio
    :param 时长: 时长
    """
    ...


def upload_group_avatar(框架QQ: int, 群号: int, pic: bytearray) -> bool:
    """
    上传群头像

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param pic: pic
    """
    ...


def upload_group_picture(框架QQ: int, 群号: int, 是否闪照: bool, pic: bytearray, 宽度: int, 高度: int, 动图: bool) -> str:
    """
    上传群图片

    成功返回图片代码

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 是否闪照: 是否闪照 是否设置为闪照
    :param pic: pic
    :param 宽度: 宽度
    :param 高度: 高度
    :param 动图: 动图 为真时可自动播放动图
    """
    ...


def upload_group_file(框架QQ: int, 群号: int, 文件路径: str, 文件夹名: str) -> str:
    """
    上传群文件

    本命令为耗时操作，请另开线程执行，本命令不支持上百mb的文件，无权限时不执行

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件路径: 文件路径 本地文件路径
    :param 文件夹名: 文件夹名 上传到哪个文件夹，填文件夹名，根目录留空或填/
    """
    ...


def upload_group_voice(框架QQ: int, 群号: int, 语音类型: int, 语音文字: str, audio: bytearray, 时长: int) -> str:
    """
    上传群语音

    成功返回语音代码

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 语音类型: 语音类型 0普通语音,1变声语音,2文字语音,3红包匹配语音
    :param 语音文字: 语音文字 文字语音填附加文字(腾讯貌似会自动替换为语音对应的文本),匹配语音填a、b、s、ss、sss，注意是小写
    :param audio: audio
    :param 时长: 时长
    """
    ...


def upload_avatar(框架QQ: int, pic: bytearray) -> str:
    """
    上传头像

    :param 框架QQ: 框架QQ
    :param pic: pic
    """
    ...


def upload_little_video(框架QQ: int, 群号: int, 本地小视频路径: str, 小视频封面图: bytearray, 宽度: int, 高度: int, 时长: int) -> str:
    """
    上传小视频

    成功返回文本代码,请另开线程调用本API,使用的手机录小视频入口,因此不支持较大文件

    :param 框架QQ: 框架QQ
    :param 群号: 群号 得到的文本代码也可在私聊使用,上传到私聊时,群号可乱填
    :param 本地小视频路径: 本地小视频路径
    :param 小视频封面图: 小视频封面图
    :param 宽度: 宽度
    :param 高度: 高度
    :param 时长: 时长
    """
    ...


def upload_photo_wall_image(框架QQ: int, pic: bytearray) -> str:
    """
    上传照片墙图片

    上传一照片至照片墙,成功返回带有‘上传成功’字样的json,失败或无权限返回json

    :param 框架QQ: 框架QQ
    :param pic: pic 图片字节集
    """
    ...


def set_as_essence(框架QQ: int, 群号: int, 消息Req: int, 消息Random: int) -> bool:
    """
    设为精华

    置指定群消息为精华内容,成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 消息Req: 消息Req
    :param 消息Random: 消息Random
    """
    ...


def set_administrator(框架QQ: int, 群号: int, 群成员QQ: int, 取消管理: bool) -> bool:
    """
    设置管理员

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ
    :param 取消管理: 取消管理 取消或设置
    """
    ...


def set_group_card(框架QQ: int, 群号: int, 群成员QQ: int, 新名片: str) -> str:
    """
    设置群名片

    置群名片

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 群成员QQ: 群成员QQ 可以是自己，无权限修改别人时会失败
    :param 新名片: 新名片
    """
    ...


def set_location_share(框架QQ: int, 群号: int, 经度: int, 纬度: int, 是否开启: bool) -> bool:
    """
    设置位置共享

    开启后需要上报位置，大约3s上报一次，否则会自动关闭，失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 经度: 经度 如：121.711540
    :param 纬度: 纬度 如：31.403343
    :param 是否开启: 是否开启
    """
    ...


def set_online_stat(框架QQ: int, main: int, sun: int, 电量: int) -> bool:
    """
    设置在线状态

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param main: main 11在线 31离开 41隐身 50忙碌 60Q我吧 70请勿打扰
    :param sun: sun 当main=11时，可进一步设置 0普通在线 1000我的电量 1011信号弱 1024在线学习 1025在家旅游 1027TiMi中 1016睡觉中 1017游戏中 1018学习中 1019吃饭中 1021煲剧中 1053汪汪汪 1032熬夜中 1050打球中 1051恋爱中 1052我没事 1028我在听歌 40001在地球 41042移动中 41033在小区 41034在学校 41035在公园 41036在海边 41037在机场 41038在商场 41039在咖啡厅 41041在餐厅 1022度假中 1020健身中 1056嗨到起飞 1058元气满满 1057美滋滋 1059悠哉哉 1060无聊中 1061想静静 1062我太难了 1063一言难尽 1064吃鸡中 1069遇见春天
    :param 电量: 电量 sun=1000时，可以设置上报电量，取值1到100，如果想显示正在充电，取值为128+电量
    """
    ...


def set_exclusive_title(框架QQ: int, 群号: int, 对方QQ: int, 头衔: str) -> bool:
    """
    设置专属头衔

    只能机器人为群主时调用

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ
    :param 头衔: 头衔 支持emoji
    """
    ...


def set_info_display(框架QQ: int, 数据: dict) -> str:
    """
    设置资料展示

    设置QQ资料卡显示什么、不显示什么

    :param 框架QQ: 框架QQ
    :param 数据: 数据 资料展示设置数据dict 传入设置数据,注意！数据每一项都必须被定义！
    """
    ...


def is_muted(框架QQ: int, 群号: int) -> int:
    """
    是否被禁言

    返回禁言时长，单位秒，[失败/无权限/未被禁言]返回0

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def pin_private(框架QQ: int, 对方QQ: int, 置顶: bool) -> bool:
    """
    私聊置顶

    成功返回true，失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 置顶: 置顶 是否置顶
    """
    ...


def send_discussion_drawing_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 题目名: str, 支付密码: str,
                                       银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组画图红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 题目名: 题目名 只能填手Q有的，如：庄周
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_discussion_solitaire_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 接龙内容: str, 支付密码: str,
                                         银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组接龙红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 接龙内容: 接龙内容 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_discussion_word_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 口令: str, 支付密码: str, 银行卡序列: int) -> tuple[
    str, dict]:
    """
    讨论组口令红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 口令: 口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_discussion_random_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 祝福语: str, 红包皮肤Id: int, 支付密码: str,
                                      银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组拼手气红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 祝福语: 祝福语 支持emoji
    :param 红包皮肤Id: 红包皮肤Id 1522光与夜之恋,1527代号:三国(打了一辈子仗),1525街霸:对决,1518代号:三国(俺送红包来了),1476天涯明月刀,1512一人之下。其他皮肤id自己找
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_discussion_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 祝福语: str, 红包皮肤Id: int, 支付密码: str,
                               银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组普通红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 祝福语: 祝福语 支持emoji
    :param 红包皮肤Id: 红包皮肤Id 1522光与夜之恋,1527代号:三国(打了一辈子仗),1525街霸:对决,1518代号:三国(俺送红包来了),1476天涯明月刀,1512一人之下。其他皮肤id自己找
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def forward_discussion_file_to_friend(框架QQ: int, 来源讨论组Id: int, 目标QQ: int, fileId: str, filename: str,
                                      filesize: int) -> Union[tuple[int, int, int], bool]:
    """
    讨论组文件转发至好友

    失败或无权限返回false 成功返回(Req, Random, time)

    :param 框架QQ: 框架QQ
    :param 来源讨论组Id: 来源讨论组Id 讨论组文件来源
    :param 目标QQ: 目标QQ
    :param fileId: fileId 文件Id
    :param filename: filename 文件名
    :param filesize: filesize 文件大小
    """
    ...


def forward_discussion_file_to_group(框架QQ: int, 来源讨论组Id: int, 目标群号: int, fileId: str, filename: str,
                                     filesize: int) -> bool:
    """
    讨论组文件转发至群

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 来源讨论组Id: 来源讨论组Id 讨论组文件来源
    :param 目标群号: 目标群号
    :param fileId: fileId 文件Id
    :param filename: filename 文件名
    :param filesize: filesize 文件大小
    """
    ...


def send_discussion_voice_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 语音口令: str, 支付密码: str,
                                     银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组语音红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 语音口令: 语音口令 支持emoji
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def send_discussion_exclusive_red_packet(框架QQ: int, 总数量: int, 总金额: int, 讨论组Id: int, 领取人: str, 祝福语: str, 是否均分: bool,
                                         支付密码: str, 银行卡序列: int) -> tuple[str, dict]:
    """
    讨论组专属红包

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 总数量: 总数量
    :param 总金额: 总金额 单位分
    :param 讨论组Id: 讨论组Id
    :param 领取人: 领取人 多个领取人QQ用|分隔
    :param 祝福语: 祝福语 支持emoji
    :param 是否均分: 是否均分 均分时每个领取人领取金额相同
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


def submit_payment_verify_code(框架QQ: int, 验证码信息: dict, 验证码: str, 支付密码: str) -> str:
    """
    提交支付验证码

    用银行卡支付时需要验证，只需要验证一次

    :param 框架QQ: 框架QQ
    :param 验证码信息: 验证码信息 验证码信息dict 银行卡发红包时传回的
    :param 验证码: 验证码 手机收到的短信验证码
    :param 支付密码: 支付密码 用于验证并支付
    """
    ...


def get_image_text(框架QQ: int, 图片地址: str) -> Union[str, bool]:
    """
    提取图片文字

    tcp，但是依然不建议频繁调用

    失败返回false

    :param 框架QQ: 框架QQ
    :param 图片地址: 图片地址 不支持https
    """
    ...


def add_friend(框架QQ: int, 对方QQ: int, 问题答案: str, 备注: str) -> str:
    """
    添加好友

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 问题答案: 问题答案 可设置回答问题答案或是验证消息，多个问题答案用"|"分隔开
    :param 备注: 备注 自定义给对方的备注
    """
    ...


def add_friend_get_verify_type(框架QQ: int, 对方QQ: int) -> str:
    """
    添加好友_取验证类型

    成功返回验证类型json,失败返回403无权限或404未找到对应框架QQ或405框架QQ未登录,ret：101已是好友 2拒绝添加 1需要身份验证 0任何人可添加 4需要回答问题,并返回所有需要回答的问题 3需要正确回答问题,并返回需要回答的问题

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def add_group(框架QQ: int, 群号: int, 验证消息: str) -> str:
    """
    添加群

    注意加群腾讯不会判断你是否在群内，你在群内或需要付费入群都会直接发送验证消息

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 验证消息: 验证消息 可设置回答问题答案或是验证消息
    """
    ...


def add_group_get_verify_type(框架QQ: int, 群号: int) -> str:
    """
    添加群_取验证类型

    获取群的加群验证信息,成功返回json retcode：1允许任何人加群 2需要验证消息 3不允许任何人加群 4回答正确问题 5回答问题并审核 如果retcode=4或5那么返回的json中retmsg有验证文本

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def double_click_avatar_friend(框架QQ: int, 对方QQ: int) -> bool:
    """
    头像双击_好友

    触发 拍一拍

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    """
    ...


def double_click_avatar_group(框架QQ: int, 对方QQ: int, 群号: int) -> bool:
    """
    头像双击_群

    触发 拍一拍 动作,被禁言时无效

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 群号: 群号
    """
    ...


def leave_discussion(框架QQ: int, 讨论组Id: int) -> bool:
    """
    退出讨论组

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id
    """
    ...


def leave_group(框架QQ: int, 群号: int) -> bool:
    """
    退群

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    """
    ...


def offline_other_device(框架QQ: int, 移动设备: bool, appid: int) -> int:
    """
    下线其他设备

    下线本QQ的其他已登录设备

    无返回值，固定返回0

    :param 框架QQ: 框架QQ
    :param 移动设备: 移动设备 若不是移动设备，可空
    :param appid: appid 若是移动设备，必填，移动设备的appid可以通过[登录事件_移动设备上线]事件来获取
    """
    ...


def offline_specified_qq(框架QQ: int) -> bool:
    """
    下线指定QQ

    敏感权限，建议使用前检查是否有权限，返回true表示成功投递下线任务，不代表对应QQ下线成功

    :param 框架QQ: 框架QQ
    """
    ...


def forward_merge_messages_to_friend(框架QQ: int, 对方QQ: int, 聊天记录: list[dict], 消息记录来源: str) -> tuple[str, int, int]:
    """
    消息合并转发至好友

    可将聊天记录合并转发给好友,支持各种消息类型,支持循环嵌套,成功返回的time可用于撤回消息

    返回(函数返回值, Random, Req)

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 聊天记录: 聊天记录 群消息数据dict列表 数组, 私聊消息数据可通过代码转换为群消息数据,复制下关键的数据内容即可
    :param 消息记录来源: 消息记录来源 可改成私聊,如:张三和李四、 张三
    """
    ...


def forward_merge_messages_to_group(框架QQ: int, 群号: int, 聊天记录: list[dict], 匿名发送: bool, 消息记录来源: str) -> str:
    """
    消息合并转发至群

    可将聊天记录合并转发到群,支持各种消息类型,支持循环嵌套

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 聊天记录: 聊天记录 群消息数据dict列表 数组, 私聊消息数据可通过代码转换为群消息数据,复制下关键的数据内容即可
    :param 匿名发送: 匿名发送 是否匿名发送聊天记录
    :param 消息记录来源: 消息记录来源 可改成私聊,如:张三和李四、 张三
    """
    ...


def edit_signature(框架QQ: int, 签名: str, 签名地点: str) -> bool:
    """
    修改个性签名

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 签名: 签名
    :param 签名地点: 签名地点 可自定义签名地点
    """
    ...


def edit_friend_note(框架QQ: int, 对方QQ: int, 备注: str) -> bool:
    """
    修改好友备注

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ 好友QQ
    :param 备注: 备注 新的备注
    """
    ...


def edit_nick(框架QQ: int, 昵称: str) -> bool:
    """
    修改昵称

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 昵称: 昵称
    """
    ...


def edit_group_name(框架QQ: int, 群号: int, 名称: str) -> bool:
    """
    修改群名称

    修改群名称,成功返回true,失败或无权限返回false,需要管理员权限

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 名称: 名称 新的群名称
    """
    ...


def edit_discussion_name(框架QQ: int, 讨论组Id: int, 新名称: str) -> bool:
    """
    修改讨论组名称

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 讨论组Id: 讨论组Id 同：群消息数据.消息群号
    :param 新名称: 新名称
    """
    ...


def edit_payment_password(框架QQ: int, 原密码: str, 新密码: str) -> str:
    """
    修改支付密码

    修改QQ钱包支付密码,成功返回json retcode=0 ,失败或无权限返回其他值

    :param 框架QQ: 框架QQ
    :param 原密码: 原密码 6位数字原密码
    :param 新密码: 新密码 6位数字新密码
    """
    ...


def edit_cached_qq_password(框架QQ: int, 新密码: str) -> bool:
    """
    修改指定QQ缓存密码

    敏感权限,无权限返回false,修改成功后,指定QQ将被下线,需要调用API【登录指定QQ】来重新登录

    :param 框架QQ: 框架QQ
    :param 新密码: 新密码
    """
    ...


def edit_personal_info(框架QQ: int, 昵称: str, 性别: int, 生日: str, 职业: int, 公司名: str, 所在地: str, 家乡: str, 邮箱: str,
                       个人说明: str) -> bool:
    """
    修改资料

    生日、家乡、所在地 参数格式和子参数数量必须正确，否则修改资料无法成功，不需要修改的项就不要填

    :param 框架QQ: 框架QQ
    :param 昵称: 昵称
    :param 性别: 性别 1:男 2:女
    :param 生日: 生日 格式：2020/5/5 均为整数
    :param 职业: 职业 1:IT,2:制造,3:医疗,4:金融,5:商业,6:文化,7:艺术,8:法律,9:教育,10:行政,11:模特,12:空姐,13:学生,14:其他职业
    :param 公司名: 公司名
    :param 所在地: 所在地 国家代码|省份代码|市代码|区字母|区代码，如：49|13110|56|NK|51，表示中国江西省吉安市青原区，这些数据是腾讯的数据，非国际数据
    :param 家乡: 家乡 国家代码|省份代码|市代码|区字母|区代码，如：49|13110|56|NI|50，表示中国江西省吉安市吉州区，这些数据是腾讯的数据，非国际数据
    :param 邮箱: 邮箱
    :param 个人说明: 个人说明
    """
    ...


def compress_7za_unzip(压缩包路径: str, 解压保存路径: str, 解压密码: str, 跳过已存在的文件: bool) -> int:
    """
    压缩包_7za解压

    无权限限制,耗时操作,请另开线程调用,支持:7z,XZ,BZIP2,GZIP,TAR,ZIP,ARJ,CAB,CHM,CPIO,DEB,DMG,FAT,HFS,ISO,LZH,LZMA,MBR,MSI,NSIS,NTFS,RAR,RPM,UDF,VHD,WIM,XAR,Z

    无返回值，固定返回0

    :param 压缩包路径: 压缩包路径 如：C:\1.zip
    :param 解压保存路径: 解压保存路径 目录路径(以\结尾),如：C:\1解压结果\
    :param 解压密码: 解压密码
    :param 跳过已存在的文件: 跳过已存在的文件 解压保存时是否自动跳过已存在的文件
    """
    ...


def compress_7za_compress(保存路径: str, 欲压缩的文件: str, 压缩格式: str, 压缩等级: int, 压缩密码: str) -> int:
    """
    压缩包_7za压缩

    无权限限制,耗时操作,请另开线程调用,支持:7z,XZ,BZIP2,GZIP,TAR,ZIP

    无返回值，固定返回0

    :param 保存路径: 保存路径 完整保存路径,如：C:\data.zip
    :param 欲压缩的文件: 欲压缩的文件 可为文件,也可为文件夹(以\结尾),如：C:\1.txt、C:\mydata\
    :param 压缩格式: 压缩格式 (7z,XZ,BZIP2,GZIP,TAR,ZIP)
    :param 压缩等级: 压缩等级 范围1-9，1为最快，9为极限
    :param 压缩密码: 压缩密码
    """
    ...


def invite_friend_to_group(框架QQ: int, 目标群号: int, 对方QQ: int, 来源群号: int) -> bool:
    """
    邀请好友加群

    拉好友或群友入群,成功返回true,失败或无权限返回false,需要群聊开启了邀请

    :param 框架QQ: 框架QQ
    :param 目标群号: 目标群号 欲邀入的群号
    :param 对方QQ: 对方QQ
    :param 来源群号: 来源群号 若对方为群友,在此填入来源群号
    """
    ...


def invite_friends_to_group(框架QQ: int, 目标群号: int, 邀请QQ: list[int], 来源群号: int) -> bool:
    """
    邀请好友加群_批量

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 目标群号: 目标群号
    :param 邀请QQ: 邀请QQ 数组, 多个邀请QQ
    :param 来源群号: 来源群号 若邀请QQ来源是群成员，则在此说明群号，否则留空，表明来源是好友
    """
    ...


def invite_friends_to_discussion(框架QQ: int, 目标讨论组Id: int, 邀请QQ: list[int], 来源群号: int) -> bool:
    """
    邀请好友加入讨论组_批量

    失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 目标讨论组Id: 目标讨论组Id
    :param 邀请QQ: 邀请QQ 数组, 多个邀请QQ
    :param 来源群号: 来源群号 若邀请QQ来源是群成员，则在此说明群号，否则留空，表明来源是好友
    """
    ...


def move_group_file(框架QQ: int, 群号: int, 文件fileid: str, 当前文件夹名: str, 目标文件夹名: str) -> str:
    """
    移动群文件

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 文件fileid: 文件fileid
    :param 当前文件夹名: 当前文件夹名 文件所在的文件夹名，根目录留空或填/
    :param 目标文件夹名: 目标文件夹名 根目录留空或填/
    """
    ...


def balance_withdrawal(框架QQ: int, 提现金额: int, 支付密码: str, 银行卡序列: int) -> str:
    """
    余额提现

    可将QQ钱包的余额提现到指定银行卡

    :param 框架QQ: 框架QQ
    :param 提现金额: 提现金额 单位分
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 指定提现到的银行卡
    """
    ...


def acc_search(框架QQ: int, 关键词: str) -> str:
    """
    账号搜索

    对一个关键词进行简略搜索,通过关键词一般返回3个QQ号信息和群信息,成功返回json retcode=0 ,失败或无权限返回其他值

    :param 框架QQ: 框架QQ
    :param 关键词: 关键词 关键词，支持QQ号、群号、昵称等，支持emoji
    """
    ...


def set_friend_verify_method(框架QQ: int, 验证方式: int, Q_and_A: str) -> bool:
    """
    置好友验证方式

    修改添加好友的方式,成功返回true,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 验证方式: 验证方式 1：禁止任何人添加 2：允许任何人添加 3：需要验证信息 4：需要正确回答问题 5：需要回答问题并由我确认
    :param Q_and_A: Q_and_A 可空,如果类型为4则填写问题和答案用‘|’分割,如果类型为5则根据情况填写问题至少一个最多三个问题,用‘|’分割
    """
    ...


def block_friend(框架QQ: int, 对方QQ: int, 是否屏蔽: bool) -> str:
    """
    置屏蔽好友

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 是否屏蔽: 是否屏蔽
    """
    ...


def set_group_note(框架QQ: int, 群号: int, 备注: str) -> bool:
    """
    置群聊备注

    成功返回true,失败返回false,无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 备注: 备注
    """
    ...


def set_group_msg_notification(框架QQ: int, 群号: int, 对方QQ: int, 通知类型: int) -> bool:
    """
    置群内消息通知

    置群内指定QQ消息通知类型,成功返回true,失败或无权限返回false

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ
    :param 通知类型: 通知类型 0不接收此人消息,1特别关注,2接收此人消息
    """
    ...


def set_group_msg_reception(框架QQ: int, 群号: int, 设置类型: int) -> bool:
    """
    置群消息接收

    失败或无权限返回false，此API未对返回结果进行分析，返回true不一定成功

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 设置类型: 设置类型 1接收并提醒 2收进群助手 3屏蔽群消息 4接收不提醒
    """
    ...


def set_special_care(框架QQ: int, 对方QQ: int, 是否关心: bool) -> str:
    """
    置特别关心好友

    :param 框架QQ: 框架QQ
    :param 对方QQ: 对方QQ
    :param 是否关心: 是否关心
    """
    ...


def group_rename_folder(框架QQ: int, 群号: int, 旧文件夹名: str, 新文件夹名: str) -> str:
    """
    重命名群文件夹

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 旧文件夹名: 旧文件夹名
    :param 新文件夹名: 新文件夹名
    """
    ...


def group_transfer(框架QQ: int, 群号: int, 对方QQ: int) -> bool:
    """
    转让群

    失败或无权限返回false,需要机器人为群主,需要新群主具备转让资格

    :param 框架QQ: 框架QQ
    :param 群号: 群号
    :param 对方QQ: 对方QQ 新群主QQ,可以是管理员、普通成员,只要对方有转让资格即可
    """
    ...


def transfer(框架QQ: int, 转账金额: int, 对方QQ: int, 转账留言: str, 转账类型: int, 支付密码: str, 银行卡序列: int) -> tuple[str, dict]:
    """
    转账

    支持向陌生人转账

    返回(函数返回值, 验证码信息dict)

    :param 框架QQ: 框架QQ
    :param 转账金额: 转账金额 单位分
    :param 对方QQ: 对方QQ
    :param 转账留言: 转账留言 支持emoji
    :param 转账类型: 转账类型 0好友转账,1陌生人转账
    :param 支付密码: 支付密码
    :param 银行卡序列: 银行卡序列 大于0时使用银行卡支付
    """
    ...


#util
def util_msg_box(提示信息: str, 图标按钮: int, 窗口标题: str) -> int:
    """
    在对话框中显示信息，等待用户单击按钮，并返回一个整数告诉用户单击哪一个按钮。该整数为 constants.信息框_用户单击_ 中的一个
    如果对话框有“取消”按钮，则按下 ESC 键与单击“取消”按钮的效果相同。

    :param 提示信息: 提示信息 显示的内容
    :param 图标按钮: 图标按钮 constants.信息框_属性_ 多个属性相加即可 除其他类外，其他属性每类只能设置一个
    :param 窗口标题: 窗口标题 信息框标题
    """
    ...


def util_input_box(提示信息: str, 窗口标题: str, 初始文本: str, 输入方式: str) -> tuple[bool, str]:
    """
    在一对话框中显示提示，等待用户输入正文并按下按钮。如果用户在确认输入后（按下“确认输入”按钮或回车键）退出，返回true，否则返回false

    :param 提示信息: 提示信息 如果提示信息太长或行数过多，超过部分将不会被显示出来
    :param 窗口标题: 窗口标题 显示在对话框标题栏中的文本
    :param 初始文本: 初始文本 初始设置到对话框输入文本框中的内容
    :param 输入方式: 输入方式 constants.输入框_输入方式_
    :return: (函数返回值, 输入框内文本)
    """
    ...


def util_usc2_to_utf8(uscStr: str) -> bytearray:
    """
    Usc2ToUtf8

    将混杂有usc2的文本转为utf8字节集

    :param uscStr: uscStr 混有usc2的文本
    """
    ...


def util_utf8_to_usc2(utf8: bytearray, 转义: bool) -> str:
    """
    Utf8ToUsc2

    将utf8编码文本转为混杂有usc2的文本，韩文等易语言不支持的文本会被转为usc2

    :param utf8: utf8 utf8编码文本
    :param 转义: 转义 是否将[\]转义回原来的样子
    """
    ...


def util_utf8_to_usc2_all(utf8: bytearray) -> str:
    """
    Utf8ToUsc2_All

    将utf8编码文本转为usc2的文本 //这个函数其实没必要 python自带

    :param utf8: utf8 utf8编码文本
    """
    ...


def util_process_msg_line_breaks(消息内容: str) -> str:
    """
    处理消息换行符

    将换行符替换为文本\r\n

    :param 消息内容: 消息内容
    """
    ...


def util_decode_response_msg_content(回复消息文本代码: str) -> str:
    """
    解码_回复消息内容

    传入回复消息文本代码 返回被回复者发送的消息内容

    :param 回复消息文本代码: 回复消息文本代码 仅支持一个
    """
    ...


def util_decode_limi_show_info(厘米秀文本代码: str) -> str:
    """
    解码_厘米秀信息

    传入厘米秀本代码 返回info字段内容

    :param 厘米秀文本代码: 厘米秀文本代码 仅支持一个
    """
    ...


def util_get_tencent_line_break(是否安卓: bool) -> str:
    """
    取腾讯换行符

    :param 是否安卓: 是否安卓
    """
    ...


def util_get_voice_download_link(语音文本代码: str) -> str:
    """
    取语音下载地址

    下载的语音大部分都是silk_v3格式，也有可能是amr格式，自行判断

    :param 语音文本代码: 语音文本代码
    """
    ...


def util_text_inversion(文本: str) -> str:
    """
    文本反转义

    将经过转义的[\]转义回来

    :param 文本: 文本
    """
    ...


def util_text_escape(文本: str) -> str:
    """
    文本转义

    将文本中[\]转义以防框架误识为文本代码

    :param 文本: 文本
    """
    ...


def util_make_cookie(QQ: int, skey: str, pskey: str) -> str:
    """
    组cookie

    容易失效，建议用clientkey登录取cookie

    :param QQ: QQ
    :param skey: skey
    :param pskey: pskey 必须和网站对应
    """
    ...


#code
def code_voice_local(文件路径: str) -> str:
    """
    语音_本地

    :param 文件路径: 文件路径 必须是silk_v3编码的文件
    """
    ...


def code_face(id: int) -> str:
    """
    小黄豆表情

    :param id: id
    """
    ...


def code_big_face(Id: int, name: str, hash: str, flag: str) -> str:
    """
    大表情

    :param Id: Id
    :param name: name
    :param hash: hash
    :param flag: flag
    """
    ...


def code_small_face(Id: int, name: str) -> str:
    """
    小表情

    :param Id: Id
    :param name: name
    """
    ...


def code_face2(id: int, name: str) -> str:
    """
    表情

    :param id: id
    :param name: name
    """
    ...


def code_emoji(表情码: str) -> str:
    """
    emoji表情 //ps:根本没用

    :param 表情码: 表情码 emoji对应的usc2代码，支持多个任意拼接
    """
    ...


def code_short_video(linkParam: str, hash1: str, hash2: str, 宽度: int, 高度: int, 时长: int) -> str:
    """
    小视频

    :param linkParam: linkParam
    :param hash1: hash1
    :param hash2: hash2
    :param 宽度: 宽度
    :param 高度: 高度
    :param 时长: 时长
    """
    ...


def code_at(对方QQ: int, 添加空格: bool) -> str:
    """
    艾特

    :param 对方QQ: 对方QQ
    :param 添加空格: 添加空格 true：添加 false：不添加 美化at显示效果
    """
    ...


def code_at_all() -> str:
    """
    艾特全体
    """
    ...


def code_pic_local(文件路径: str) -> str:
    """
    图片_本地

    :param 文件路径: 文件路径
    """
    ...


def code_flash_pic_local(文件路径: str) -> str:
    """
    闪照_本地

    :param 文件路径: 文件路径
    """
    ...


def code_shake(Id: int, Type: int, name: str) -> str:
    """
    抖一抖

    :param Id: Id
    :param Type: Type
    :param name: name
    """
    ...


def code_limi_show(Id: int, Type: int, name: str, info: str) -> str:
    """
    厘米秀

    :param Id: Id
    :param Type: Type
    :param name: name
    :param info: info
    """
    ...


def code_reply(对方发送内容: str, 对方QQ: int, 消息接收时间: int, 消息req: int, 消息random: int) -> str:
    """
    回复消息

    :param 对方发送内容: 对方发送内容
    :param 对方QQ: 对方QQ
    :param 消息接收时间: 消息接收时间
    :param 消息req: 消息req
    :param 消息random: 消息random
    """
    ...


def code_flash_word(desc: str, resid: str, prompt: str) -> str:
    """
    闪字

    :param desc: desc
    :param resid: resid
    :param prompt: prompt 闪字内容，注意此处不支持其他文本代码
    """
    ...


def code_honest(对方QQ: int, 对方昵称: str, 描述: str, 发送时间: str, 发送Random: str, 背景类型: int) -> str:
    """
    坦白说

    :param 对方QQ: 对方QQ 可自定义
    :param 对方昵称: 对方昵称 可自定义
    :param 描述: 描述 可自定义
    :param 发送时间: 发送时间 10位时间戳，可自定义
    :param 发送Random: 发送Random 可自定义
    :param 背景类型: 背景类型 可自定义，不同背景对应的值日志查看
    """
    ...


def code_graffiti(模型Id: int, 涂鸦hash: str, 涂鸦图片地址: str) -> str:
    """
    涂鸦

    :param 模型Id: 模型Id 手机QQ上涂鸦背景从左往右数，从0开始
    :param 涂鸦hash: 涂鸦hash 和图片地址对应
    :param 涂鸦图片地址: 涂鸦图片地址 和hash对应
    """
    ...


def code_pic_show(图片hash: str, 秀图类型: int, 宽度: int, 高度: int, 动图: bool) -> str:
    """
    秀图

    :param 图片hash: 图片hash 通过群图片代码获得
    :param 秀图类型: 秀图类型 40000普通,40001幻影,40002抖动,40003生日,40004爱你,40005征友
    :param 宽度: 宽度
    :param 高度: 高度
    :param 动图: 动图 为真时可自动播放动图
    """
    ...


def code_custom_dice(骰子点数: int) -> str:
    """
    自定义骰子

    :param 骰子点数: 骰子点数
    """
    ...


def code_stick(X值: str, Y值: str, 粘贴内容宽值: str, 粘贴内容高值: str, 粘贴倾角: str, 消息接收时间: int, 消息req: int, 消息random: int) -> str:
    """
    粘贴消息

    :param X值: X值 与粘贴位置有关,由横向位置经过特定算法得到
    :param Y值: Y值 与粘贴位置有关,由纵向位置经过特定算法得到
    :param 粘贴内容宽值: 粘贴内容宽值 可决定粘贴内容的宽度,由缩放宽度经过特定算法得到
    :param 粘贴内容高值: 粘贴内容高值 可决定粘贴内容的高度,由缩放高度经过特定算法得到
    :param 粘贴倾角: 粘贴倾角 粘贴内容与水平位置的倾角
    :param 消息接收时间: 消息接收时间
    :param 消息req: 消息req
    :param 消息random: 消息random
    """
    ...


def code_custom_guess(类型: int) -> str:
    """
    自定义猜拳

    :param 类型: 类型 1石头,2剪刀,3布
    """
    ...


def code_contact(Type: int, 分享账号: int) -> str:
    """
    分享名片

    :param Type: Type 0为群分享,其他则为好友分享
    :param 分享账号: 分享账号 Type为0则表示QQ号,Type为其他则表示群号
    """
    ...
