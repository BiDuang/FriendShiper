import requests
import constants
import tools
import xlz

mojangurl = "https://api.mojang.com/users/profiles/minecraft/"
apiurl = "https://api.biduang.cn/fserplayersdata/"


def startup():
    data = {
        'name': 'FserStatistics',  # 插件名称,str,必需
        'author': 'BiDuang',  # 作者,str,必需
        'version': 'Released',  # 版本号,str,必需
        'description': '服务器统计',  # 简介,str,必需
        'func_group': group,  # 群聊消息处理函数
    }
    return data


def group(data: dict):
    data: dict = tools.process_negative_int_obj(data)  # 处理负整数

    if (data['self_qq'] != data['sender_qq']) and (data['self_anon_id'] != data['sender_qq']):

        if data['msg_type'] != constants.消息类型_讨论组消息:
            if data['message'].startswith('损坏查询 '):
                player = data['message'][5:]
                msg = getplayerinfo(player, 0)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('战斗查询 '):
                player = data['message'][5:]
                msg = getplayerinfo(player, 1)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('合成查询 '):
                player = data['message'][5:]
                msg = getplayerinfo(player, 2)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('开采查询 '):
                player = data['message'][5:]
                msg = getplayerinfo(player, 3)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('移动查询 '):
                player = data['message'][5:]
                msg = getplayercustinfo(player, 0)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('游戏时间查询 '):
                player = data['message'][7:]
                msg = getplayercustinfo(player, 1)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('村民交易查询 '):
                player = data['message'][7:]
                msg = getplayercustinfo(player, 2)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)
            elif data['message'].startswith('昏睡查询 ') or data['message'].startswith('睡觉查询 '):
                player = data['message'][5:]
                msg = getplayercustinfo(player, 3)
                xlz.send_group_msg(
                    data['self_qq'], data['from_group'], msg, False)

    return False


def getplayeruuid(user: str):
    r = requests.get(f"{mojangurl}{user}")
    fsr = requests.get(f"{apiurl}whitelist/whitelist.json")
    fswl = eval(fsr.text)

    try:
        curusr = eval(r.text)
    except SyntaxError:
        return '错误的用户名称，请确认是否是Minecraft正版玩家'
    p1 = curusr['id'][:8].strip()+'-'
    p2 = curusr['id'][8:12].strip()+'-'
    p3 = curusr['id'][12:16].strip()+'-'
    p4 = curusr['id'][16:20].strip()+'-'
    p5 = curusr['id'][20:len(curusr['id'])].strip()
    uuid = p1+p2+p3+p4+p5

    inplayers = []
    for player in fswl:
        inplayers.append(player['uuid'])

    if uuid not in inplayers:
        return '该用户不是一位朋友船船员'

    curusr['id'] = uuid
    return curusr


def getplayerdata(user: str):
    usrd = getplayeruuid(user)
    if type(usrd) == str:
        return usrd

    r = requests.get(f"{apiurl}{usrd['id']}.json")
    usrdata = eval(r.text)

    return usrdata


def getplayerinfo(user: str, mode: int):
    usrdata = getplayerdata(user)
    if type(usrdata) == str:
        return usrdata

    try:
        if mode == 0:
            sum = 0
            for i in usrdata['stats']['minecraft:broken'].values():
                sum += i

            a = sorted(usrdata['stats']['minecraft:broken'].items(
            ), key=lambda x: x[1], reverse=True)
            topbrk = a[0][0]
            ret = f"{user}在本周目的Friendship Minecraft服务器中，共损坏了{sum}个装备\n其中，损坏最多的是{topbrk}"
            return ret
        if mode == 1:
            sum = 0
            for i in usrdata['stats']['minecraft:killed_by'].values():
                sum += i

            a = sorted(usrdata['stats']['minecraft:killed_by'].items(
            ), key=lambda x: x[1], reverse=True)
            top = a[0][0]
            sum1 = 0
            for i in usrdata['stats']['minecraft:killed'].values():
                sum1 += i

            a = sorted(usrdata['stats']['minecraft:killed'].items(
            ), key=lambda x: x[1], reverse=True)
            top1 = a[0][0]
            ret = f"{user}在本周目的Friendship Minecraft服务器中，击杀了{sum1}个实体，被实体杀死了{sum}次\n{user}杀死最多的次实体是{top1}，而被{top}杀了最多次"
        if mode == 2:
            sum = 0
            for i in usrdata['stats']['minecraft:crafted'].values():
                sum += i

            a = sorted(usrdata['stats']['minecraft:crafted'].items(
            ), key=lambda x: x[1], reverse=True)
            topbrk = a[0][0]
            ret = f"{user}在本周目的Friendship Minecraft服务器中，共合成或加工了{sum}次物品\n其中，{user}合成加工最多的物品是{topbrk}"
            return ret
        if mode == 3:
            sum = 0
            for i in usrdata['stats']['minecraft:mined'].values():
                sum += i

            a = sorted(usrdata['stats']['minecraft:mined'].items(
            ), key=lambda x: x[1], reverse=True)
            topbrk = a[0][0]
            ret = f"{user}在本周目的Friendship Minecraft服务器中，共开采了{sum}个方块\n其中，{user}开采最多的方块是{topbrk}"
            return ret
    except KeyError:
        return '没有查找到该玩家的此项数据'

    if mode == 1 and 'minecraft:player_kills' in usrdata['stats']['minecraft:custom'].keys():
        ret += f"\n并且，其中{user}击杀的玩家数为{usrdata['stats']['minecraft:custom']['minecraft:player_kills']}"
    else:
        ret += f"\n并且，{user}还没有参与过PVP"
    return ret


def getplayercustinfo(user: str, mode: int):
    usrdata = getplayerdata(user)
    if type(usrdata) == str:
        return usrdata

    try:
        if mode == 0:
            walkd = format((usrdata['stats']['minecraft:custom']['minecraft:walk_one_cm'] +
                           usrdata['stats']['minecraft:custom']['minecraft:sprint_one_cm'])/1000, '.2f')
            flyd = format((usrdata['stats']['minecraft:custom']['minecraft:fly_one_cm'] +
                          usrdata['stats']['minecraft:custom']['minecraft:aviate_one_cm'])/1000, '.2f')
            ret = f"{user}在本周目的Friendship Minecraft服务器中共走了{walkd}千米，飞行了{flyd}千米"
            return ret
        if mode == 1:
            newver = False
            try:
                playtime = int(
                    usrdata['stats']['minecraft:custom']['minecraft:play_time'])
                newver = True
            except KeyError:
                playtime = int(
                    usrdata['stats']['minecraft:custom']['minecraft:play_one_minute'])
            playtime /= 20*60
            playhrs = playtime/60
            playdys = playhrs/24

            playtime = float(format(playtime, '.2f'))
            playhrs = float(format(playhrs, '.2f'))
            playdys = float(format(playdys, '.2f'))

            if playtime >= 1 and playhrs < 1:
                ret = f"{user}在本周目的Friendship Minecraft服务器中的共计游戏时间为{playtime}分钟"
            elif playhrs >= 1 and playdys < 1:
                ret = f"{user}在本周目的Friendship Minecraft服务器中的共计游戏时间为{playhrs}小时"
            elif playdys >= 1:
                ret = f"{user}在本周目的Friendship Minecraft服务器中的共计游戏时间为{playdys}天"
            else:
                ret = f"{user}在本周目的Friendship Minecraft服务器中的游玩时间不足一分钟"

            if newver:
                ret = ret+'\n而且，该玩家登录过了1.17版本的FriendShip X P3服务器'
            else:
                ret = ret+'\n而且，该玩家还没登录过1.17版本的FriendShip X P3服务器'

            return ret
        elif mode == 2:
            ret = f"{user}在本周目的Friendship Minecraft服务器中曾{usrdata['stats']['minecraft:custom']['minecraft:talked_to_villager']}次尝试与村民交易"
            return ret
        elif mode == 3:
            outp = f"{user}在本周目的Friendship Minecraft服务器中昏睡了{usrdata['stats']['minecraft:custom']['minecraft:sleep_in_bed']}次~"
            slptime = usrdata['stats']['minecraft:custom']['minecraft:time_since_rest']
            slptime /= 20*60
            slphrs = slptime/60

            slptime = float(format(slptime, '.2f'))
            slphrs = float(format(slphrs, '.2f'))

            if slptime >= 1 and slphrs < 1:
                ret = f"{user}距离上一次在游戏睡觉已经过去了{slptime}分钟"
            elif slphrs >= 1:
                ret = f"{user}距离上一次在游戏睡觉已经过去了{slphrs}小时"
            else:
                ret = f"{user}距离上一次在游戏睡觉还不足一分钟"
            ret = outp+'\n'+ret
            return ret
    except KeyError:
        return '没有查找到该玩家的此项数据'
