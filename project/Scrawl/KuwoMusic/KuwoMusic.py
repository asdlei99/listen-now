# __date__ 2018/7/29
# __file__ KuwoMusic
# __author__ Msc
# encoding:utf-8

import requests
import re
import json
import copy
import simplejson
from project.Module import ReturnStatus
from project.Module import RetDataModule

class KuwoMusic(object):
    '''
        酷我音乐
    '''
    re_dict = copy.deepcopy(RetDataModule.mod_search)
    def __init__(self):
        self.baseurl = "http://search.kuwo.cn/r.s?all=%s&ft=music&itemset=web_2013&client=kt&pn=%s&rn=%s&rformat=json&encoding=utf8"
        self.searchurl = "http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId=%s"
        self.palyurl = "http://antiserver.kuwo.cn/anti.s?type=convert_url&rid=%s&format=aac|mp3&response=url"
        self.commenturl = "http://comment.kuwo.cn/com.s?type=get_comment&uid=0&prod=newWeb&digest=15&sid=%s&page=1&rows=10&f=web"
        self.session = requests.session
        self.header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer':base_0url
        }

    def Search_List(self,keyword,page,num = 10) -> str:

        re_dict = copy.deepcopy(RetDataModule.mod_search)
        try:
            resp = eval(self.session.get(url=self.baseurl%(keyword,page,num),headers=self.headers).text)
        except simplejson.error.JSONDecodeError:
            re_dict["code"] = ReturnStatus.ERROR_SEVER
            return re_dict
        try:
            for item in resp["abslist"]:
                count += 1
                singer = item["artist"]
                songname = item["songname"]
                music_id = item["musicrid"][6:]
                return_dict = {"music_name":songname,"artist":singer,"id":musicrid}
                re_dict["song"]["list"].append(return_dict)
            re_duct["song"]["totalnum"] = count
            return re_dict

    def Search_details(self,music_id):
        
        re_dict = copy.deepcopy(RetDataModule.mod_song)
        try:
            resp = eval(self.session.get(url=self.searchurl%(music_id),headers=self.headers).text)
        except simplejson.errors.JSONDecodeError:
            re_dict["code"] = ReturnStatus.ERROR_SEVER
            return re_dict 

        try:
            re_dict["music_id"] = resp["data"]["songinfo"]["id"]
            re_dict["music_name"] = resp["data"]["songinfo"]["songName"]
            re_dict["artists"] = resp["data"]["songinfo"]["artist"]
            re_dict["play_url"] = self.get_play_url(music_id)
            re_dict["lyric"] = resp["data"]["songinfo"]["lrclist"]
            re_dict["image_url"] = resp["data"]["songinfo"]["pic"]
            re_dict["comment"] = self.get_comment(music_id)
        except:re_dict["code"]    = ReturnStatus.DATA_ERROR
        else:re_dict["code"]      = ReturnStatus.SUCCESS
        return re_dict


    def get_play_url(self,music_id):
        re_dict = copy.deepcopy(RetDataModule.mod_song)

        play_url = "http://antiserver.kuwo.cn/anti.s?type=convert_url&rid={0}&format=aac|mp3&response=url".format(music_id)
        return play_url


    def get_comment(self,music_id):
        resp = eval(self.session.get(url=self.commenturl%(music_id),headers=self.headers).text)
        comment = resp["rows"]
        return comment




if __name__=="__main__":

    test = KuwoMusic()

    rest.Search_List("青花瓷",1)










