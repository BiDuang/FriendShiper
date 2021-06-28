import requests
import constants
import tools
import xlz

url = 'https://api.biduang.cn/fserstat/index.php'


def startup():

    data = {
        'name': 'FserStatChecker',  # 插件名称,str,必需
        'author': 'BiDuang',  # 作者,str,必需
        'version': 'Alpha-55',  # 版本号,str,必需
        'description': '朋友船服务器状态获取',  # 简介,str,必需
        'func_group': group,  # 群聊消息处理函数
    }
    return data


accpet_command = {'olplayers': '服务器在线玩家', 'stat': '服务器状态', 'ver': '服务器版本'}


def group(data: dict):
    data: dict = tools.process_negative_int_obj(data)  # 处理负整数

    if (data['self_qq'] != data['sender_qq']
            ) and (data['self_anon_id'] != data['sender_qq']):

        if data['msg_type'] != constants.消息类型_讨论组消息:
            if data['message'] in accpet_command.values():
                if chkfseronline():
                    if data['message'].strip() == accpet_command['olplayers']:
                        msg = getfseronline(data)

                    elif data['message'].strip() == accpet_command['stat']:
                        msg = getfserstat()

                    elif data['message'].strip() == accpet_command['ver']:
                        msg = getfserversion()

                    xlz.send_group_msg(
                        data['self_qq'], data['from_group'], msg, False)
                else:
                    xlz.send_group_msg(
                        data['self_qq'], data['from_group'], ':( \n未能获取到服务器信息\n原因可能是服务器离线、冰冰Api系统离线、机器人故障\n请联系管理员以获取更多帮助', False)
    return False


def getfseronline(data: dict):

    webdict = getwebdata()

    if webdict['online'] == 'NUL':
        return ':( \n服务器空无一人\n你可以稍后再查询'
    else:
        onlineplayers = list(webdict['online'])
        outp = ''
        for player in onlineplayers:
            playerimg = bytearray(requests.get(
                f'https://cravatar.eu/helmhead/{player}/35.png').content)
            outp = outp+player+xlz.upload_group_picture(
                data['self_qq'], data['from_group'], False, playerimg, 0, 0, False)+'\n'
        strlen = len(outp)-1
        outp = '目前服务器有'+str(webdict['server']['Players'])+'/' + \
            str(webdict['server']['MaxPlayers'])+'名在线玩家：\n'+outp[:strlen]
    return outp


def chkfseronline():
    webdict = getwebdata()
    if webdict['result'] != 'success':
        return False
    else:
        return True


def getfserstat():
    webdict = getwebdata()
    serverdict = webdict['server']
    outp = f"FriendShip服务器在{webdict['timer']}s内响应了查询\n服务器Motd：{serverdict['Motd']}"
    return outp


def getfserversion():
    webdict = getwebdata()
    serverdict = webdict['server']
    outp = f"服务器目前运行在{serverdict['Version']}版本的{serverdict['GameName']}上"
    return outp


def getwebdata():
    header = {'Connection': 'close'}
    r = requests.get(url, headers=header)
    webdict = eval(r.text)
    return webdict
