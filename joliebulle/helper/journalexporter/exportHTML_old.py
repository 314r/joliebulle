#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


from PyQt5.QtCore import QCoreApplication




def exportHTML(itemsList):
    resultHtml = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>Journal</title>
<meta charset="utf-8" />
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
    <style>
    body {background:url(images/furley_bg.png);}
    .journal {width:800px;margin:auto;padding-top:0.5em;padding-bottom:1em;}
    .journal h1{color:#999;font-weight:bold;margin:auto;padding-top:0.1em; font-size:24px ;float:left;}
    .journal-list{margin:auto;margin-top:3em; margin-bottom:3em; background-color: white; width:800px;border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);padding: 50px;}
    .entry{min-height:3em;}
    .date{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;color:white; font-size:85%%; font-weight: bold;}
    .entry button{color:white;}
    .entry:hover button{color:#428bca;}
    .event{padding-right:20px;}
    </style>
</head>
<body>
'''


    resultHtml +=''' <div class="journal">
                        <h1>Journal</h1>
                    </div>
                    <div class="journal-list"></div>'''


    # i=0
    # for entry in itemsList :
    #     i=i+1
    #     resultHtml += '''<div class="entry" id="%s">%s <button type="button" value="delete" onClick="main.delJournal(%s);deleteEntry(%s)" > <i class="icon-wrench"></i> Supprimer </button></div>''' %(i,entry["recipe"],i,i)

    resultHtml += '''<script src="jquery/jquery.js"></script>
                     <script src="mustache/mustache.js"></script>
                     '''

    resultHtml += ''' <script type="text/javascript">
                    function deleteEntry(id) {
                    $("#" + id).remove();
                    }
                </script>'''

    resultHtml += '''<script type="text/javascript">

                        var entryLists = %s
                        for(var i=0;i<entryLists.length;i++)
                            {
                                tableau=entryLists[i];
                                date= new Date();
                                date.setTime(tableau["date"]*1000);
                                date = ('0'+date.getDate()).slice(-2) + '/' + ('0'+(date.getMonth() + 1)).slice(-2) + '/' + date.getFullYear();
                                event = "'" + tableau["event"] + "'"
                                recipe = "'" + tableau["recipe"] + "'"
                                stringSignal = tableau["date"] + ',' + event + ',' + recipe
                                console.log(event)
                                $(".journal-list").append("<div class =%s id="+i+">" + '<span class="date">'+ date + ' </span>' + tableau["recipe"] + ' %s <span class="event">' + tableau["event"] + '.</span><button class="btn btn-link btn-xs" type="button" value="delete" onClick="main.delJournal('+tableau["date"]+');deleteEntry('+i+ ')" > %s </button><button class="btn btn-link btn-xs" type="button" value="delete" onClick="main.editJournalEntry('+stringSignal+')" > %s </button></div>');

                            }
                     </script>''' %(str(itemsList), "entry",QCoreApplication.translate("Export","a été marquée comme"),QCoreApplication.translate("Export","Supprimer"),QCoreApplication.translate("Export","Modifier"))





    # resultHtml += ''' <script type="text/javascript">
    #                 $(".entry").append('coincoin');
    #             </script>'''
    # resultHtml+='''<script type="text/javascript">
    # var data = {title: "Javascript: the Good Parts", author: "Douglas Crockford"};
    # var template = 'Title: <b>{{title}}</b> <br/> Author: {{author}}';
    # var output = Mustache.render(template, data);
    # $(".entry").append(output);
    # </script>'''

    resultHtml += ''' </body></html>'''

    return resultHtml
