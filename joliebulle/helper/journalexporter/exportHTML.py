#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.0
#Copyright (C) 2010-2013 Pierre Tavares
#Copyright (C) 2013 Thomas Gerbet

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


from PyQt4.QtCore import QCoreApplication




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

    </style>
</head>
<body>
'''    
    

    resultHtml +=''' <div class="container"></div>'''


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
                                date = date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear();
                                event = tableau["event"]
                                $(".container").append("<div class =%s id="+i+">" + '<span class="date">'+ date + '</span>' + tableau["recipe"] + '<span class="event">' + event + '</span>' +'<button type="button" value="delete" onClick="main.delJournal('+tableau["date"]+');deleteEntry('+i+ ')" > Supprimer </button>' +"</div>");

                            }
                     </script>''' %(str(itemsList), "entry")





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


