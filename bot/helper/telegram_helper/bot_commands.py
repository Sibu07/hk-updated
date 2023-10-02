#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'm{CMD_SUFFIX}', f'mirror{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qm{CMD_SUFFIX}', f'qbmirror{CMD_SUFFIX}']
        self.YtdlCommand = [f'y{CMD_SUFFIX}', f'ytdl{CMD_SUFFIX}']
        self.LeechCommand = [f'l{CMD_SUFFIX}', f'leech{CMD_SUFFIX}']
        self.QbLeechCommand = [f'ql{CMD_SUFFIX}', f'qbleech{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'yl{CMD_SUFFIX}', f'ytdlleech{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'uzm{CMD_SUFFIX}', f'unzipmirror{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}', f'zm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'quzm{CMD_SUFFIX}', f'qbunzipmirror{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}', f'qzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'yz{CMD_SUFFIX}', f'ytdlzip{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'uzl{CMD_SUFFIX}', f'unzipleech{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'quzl{CMD_SUFFIX}', f'qbunzipleech{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'yzl{CMD_SUFFIX}', f'ytdlzipleech{CMD_SUFFIX}'])
        self.CloneCommand = [f'c{CMD_SUFFIX}', f'clone{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = f'can{CMD_SUFFIX}'
        self.CancelAllCommand = [f'canall{CMD_SUFFIX}', 'canall']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f's{CMD_SUFFIX}', f'status{CMD_SUFFIX}', 's']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'auth{CMD_SUFFIX}', f'auth']
        self.UnAuthorizeCommand = [f'unauth{CMD_SUFFIX}', f'unauth']
        self.AddBlackListCommand = [f'bl{CMD_SUFFIX}', f'blacklist{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rbl{CMD_SUFFIX}', f'rmblacklist{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'p{CMD_SUFFIX}', 'ping']
        self.RestartCommand = [f'rt{CMD_SUFFIX}', f'restart{CMD_SUFFIX}', 'rtall']
        self.StatsCommand = [f'st{CMD_SUFFIX}', f'stats{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bs{CMD_SUFFIX}', f'bsall']
        self.UserSetCommand = [f'us{CMD_SUFFIX}', f'usall']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'sp{CMD_SUFFIX}', f'speedtest{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mi{CMD_SUFFIX}', f'mediainfo{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gc{CMD_SUFFIX}', f'gdclean{CMD_SUFFIX}']
        self.BroadcastCommand = [f'bc{CMD_SUFFIX}', f'broadcast{CMD_SUFFIX}']

BotCommands = _BotCommands()
