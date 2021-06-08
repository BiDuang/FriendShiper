"""
FriendShiper Plugin by BiDuang
"""

from os import close
import os.path
import json
import datetime
import constants
import tools
import xlz
import codecs


# 尽量避免在此处放置初始化代码，请在初始化或插件被启用事件进行初始化


def startup():
    # 获取插件数据存放目录
    global filename
    data_folder = xlz.get_data_folder() + 'friendshiper\\'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    filename = data_folder+'event_data.json'

    data = {
        'name': 'FriendShiper',  # 插件名称,str,必需
        'author': 'BiDuang',  # 作者,str,必需
        'version': 'Beta-23',  # 版本号,str,必需
        'description': '基于FirendShip群聊的消息处理系统',  # 简介,str,必需
        'func_group': group,  # 群聊消息处理函数
    }
    return data


def group(data: dict):
    global event_dict
    global f
    data: dict = tools.process_negative_int_obj(data)  # 处理负整数
    f = codecs.open(filename, "r", 'utf-8')
    event_dict = eval(f.read())
    f.close()
    usrpr = group_permission_check(data['sender_qq'], data)

    if (data['self_qq'] != data['sender_qq']) and (data['self_anon_id'] != data['sender_qq']):  # 过滤自己(包括其他设备)的消息
        if data['msg_type'] != constants.消息类型_讨论组消息:

            if data['message'].startswith('群事件列表'):
                group_event_check(data['message'], data)

            elif data['message'].startswith('添加群事件'):

                group_event_ctrl(data, 1, data['message'], usrpr)

            elif data['message'].startswith('删除群事件'):
                group_event_ctrl(data, 2, data['message'], usrpr)

    return False


def group_event_ctrl(data: dict, mode: int, message: str, perm: bool):
    if perm != True:
        xlz.send_group_msg(
            data['self_qq'], data['from_group'], '你需要管理员权限来执行该操作！', False)
        return
    if mode == 1:  # 添加群事件操作
        if data['message'].strip() == '添加群事件':
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], '这个指令需要你提供足够的参数！', False)
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], '格式：添加群事件 (事件名) (日期)\n日期请用"-"作为年月日的分隔符', False)
            return
        else:
            lines = message[5:].split(" ")
            try:
                etitle = lines[1].strip()
                edate = lines[2].strip()
            except IndexError:
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], '这个指令需要你提供足够的参数！', False)
                return
            if edate < datetime.datetime.now().strftime('%Y-%m-%d'):
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], '注意：你添加了一个过去的事件', False)
            msg = "成功添加将在 " + edate + " 举行的群事件:" + etitle
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], msg, False)
            event_dict[etitle] = edate
            f = codecs.open(filename, "w", "utf-8")
            f.write(str(event_dict))
            f.close()
    elif mode == 2:
        if data['message'].strip() == '删除群事件':
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], '这个指令需要你提供足够的参数！', False)
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], '格式：删除群事件 (事件名)', False)
            return
        else:
            lines = message[5:].split(" ")
            etitle = lines[1].strip()
            xlz.log(etitle, '#000000', '#ffffff')
            try:
                event_dict.pop(etitle)
            except IndexError:
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], '你指定的事件不存在！', False)
                return

            msg = '你已经成功删除'+etitle+'！'
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], msg, False)
            f = codecs.open(filename, "w", "utf-8")
            f.write(str(event_dict))
            f.close()


def group_event_check(message: str, data: dict):
    message = message[5:]
    if message != '':
        try:
            line = int(message)
        except ValueError:
            xlz.send_group_msg(
                data['self_qq'], data['from_group'], '你需要提供一个整数作为参数!', False)
            return
    else:
        roll = True
    eventname = list(event_dict.keys())
    eventdate = list(event_dict.values())

    if roll:
        outp = '共有'+str(len(eventname))+'个事件；\n'
        rep = ''
        ct = 1
        for i in event_dict.keys():
            rep = rep + str(ct)+"：" + str(eventname[ct-1])+"\n"
            ct += 1
        outp = outp+rep
    else:
        try:
            outp = str(line)+'\n在' + \
                str(eventdate[line-1])+'有群事件：\n'+str(eventname[line])
        except IndexError:
            outp = '你指定的事件不存在'
    xlz.send_group_msg(
        data['self_qq'], data['from_group'], outp, False)


def group_permission_check(req: int, data: dict):
    # 获取群管理员列表
    adminstr = xlz.get_administrator_list(
        data['self_qq'], data['from_group']).strip()
    adminlist = []
    lines = adminstr.split("\n")
    for line in lines:
        adminlist.append(int(line.strip()))
    adminlist.append(2267304497)  # 调试专用

    ret = '用户 ' + str(req) + ' 通过了权限检查'
    if req in adminlist:  # 权限检查
        xlz.log(ret, '#000000', '#ffffff')
        return True
    else:
        return False
