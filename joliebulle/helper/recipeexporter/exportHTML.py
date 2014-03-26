#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.2
#Copyright (C) 2010-2014 Pierre Tavares
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


def exportHTML(data):
    resultHtml = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="jquery/jquery.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="underscore/underscore-min.js"></script>
<script src="controllers/recipe/main.js"></script>
<script src="controllers/recipe/recipe.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="css/sidebar.css">
<link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.4.3.min.css">
<script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="http://cdn.oesmith.co.uk/morris-0.4.3.min.js"></script>
<style>
    .recipe-header {padding-left:30px;}
    .recipe-header h1 { font-size:18px; color:#444;padding-top:15px;padding-bottom:30px;padding-left:0;}
    .recipe-vol {padding-left:30px;padding-top:30px;}
    .vol-label {color: #bbb;}
    .vol-value {background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    .effi-label {color: #bbb;}
    .effi-value {background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    
    .recipe-infos{border-bottom:solid 1px #eee;padding-bottom:0px;padding-left: 10px;}
    .profile-sidebar h5 {padding-left: 20px;margin-top:25px; padding-top:9px;padding-bottom:9px;background:#fff;color:#6f6f6f;font-weight: 800;}
    .recipe-infos-list li{list-style-type: none;color:#6f6f6f;padding-top:14px;}
    ul.recipe-infos-list{padding-left:20px; padding-top:0;}
    
    .recipe-buttons{margin-left:30px;/*border-bottom:solid 1px #eee;*/padding-top: 33px;padding-left:5px;}
    .edit-button{/*color:#f55050;*/ color:#7ca3fa;padding-right: 20px;}
    .tools-recipe{color:#222;float:right;font-size:18px;}
    .ibu {color:#7ca3fa;}
    .ebc {color:#7ca3fa;}
    .gravity {color:#7ca3fa;}
    .alc {color:#7ca3fa;}
    .ing{padding-bottom:1.5em;}
    .grains{padding-left:30px;}
    .grains h3 {padding-bottom:18px; color:#bbb ; padding-top:40px;}
    .hops {padding-left:30px;}
    .hops h3 {padding-bottom:18px; padding-top:30px;color:#bbb}
    .yeasts {padding-left:30px;}
    .yeasts h3 {padding-bottom:18px;padding-top:30px;color:#bbb}
    #donutchart{padding:0;margin:0;margin-top:-3.5em;}
    #hopbar{margin-left:-20px;}
    .profile p{margin-bottom: 1.5em;}
    .profile-name{font-weight: bold;display:block;}
    .label-step{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:white; font-size:85%%; font-weight: bold;}
    .label-sparge{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:white; font-size:85%%; font-weight: bold;}
    .profile-ph{display:inline-block;margin-top:1em;margin-bottom:1.5em;background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    #profile-graph{margin-top:2em;}

    .notes{margin-bottom:90px;}

    .row-journal{padding-left: 15px; padding-right: 15px;}
    .entry{min-height:3em;}
    .date{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;color:white; font-size:85%%; font-weight: bold;}
    .entry button{color:white;}
    .entry:hover button{color:#428bca;}
    .event{padding-right:20px;}
    .newButton{padding: 10px 0 18px; margin-top:100px;}
    .newButton button {background:#f7f7f7; border:none; color:#6f6f6f;margin-left:0px;padding:5px 10px 5px 10px;}
    /*.newButton button:hover{color:#333333;}*/
    .new-form {margin-bottom:1em;padding: 50px;padding-top: 1em; padding-bottom:1em;}
    .entry .saveButton {color:#428bca;}
</style>
</head>'''

    resultHtml += '''
<body ng-app="recipe">


    <div class="container-fluid" ng-controller="RecipeCtrl" ng-init='init({0})'>
    ''' .format(data)

    resultHtml += '''
        
        
        <div class="sidebar col-sm-3 col-md-2 col-lg-2">
            <ul class="nav nav-sidebar">
                <li class="active"><a href="#"><i class="icon-beaker"></i> Recettes</a></li>
                <li><a href="#"><i class="icon-calendar-empty"></i> Journal</a></li>
                <li><a href="#"><i class="icon-cog"></i> Outils</a></li>
            </ul>
            
            <div class="profile-sidebar">
                <h5>Profil</h5>
                <ul class="recipe-infos-list">
                    <li data-toggle="tooltip" data-placement="right" title="Amertume"><span class="ibu">{{recipe.ibu}}</span> IBU</li>
                    <li><span class="ebc">{{recipe.ebc}}</span> EBC</li>
                    <li><span class="gravity">{{recipe.og}}</span> DI</li>
                    <li><span class="gravity">{{recipe.fg}}</span> DF</li>
                    <li><span class="alc">{{recipe.bugu}}</span> BU/GU</li>
                    <li><span class="alc">{{recipe.alc}} %</span> Alc</li>
                </ul>
            </div>
        </div>
        
        <div class="col-md-10 col-md-offset-2 main">
                   
            <div class="recipe-header row">
                <h1 class="col-md-5">{{recipe.name}}</h1>
                <div class="recipe-buttons col-md-5">
                    <button class="btn-link  edit-button" type="button" data-toggle="dropdown" ><i class="icon-flag"></i> Journal <span class="icon-caret-down"></span></button>
                    <ul class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">%s :</i>
                                <li><a onClick="main.addToJournal('brewed')" href="#">%s</a></li>
                                <li><a onClick="main.addToJournal('ferment')" href="#">%s</a></li>
                                <li><a onClick="main.addToJournal('bottled')" href="#">%s</a></li>
                                <li class="divider"></li>
                                <li><a onClick="main.showJournal()" href="#">%s</a></li>
                              </ul>
                    <button class="btn-link  edit-button" type="button" ><i class="icon-wrench"></i> Editer la recette </button>
                </div>
            </div>
            
            <div class="recipe-vol">
                <span class="vol-label">Vol</span> <span class="vol-value">{{recipe.volume}}L</span>
                <span class="effi-label"> Rendement</span> <span class="effi-value">{{recipe.efficiency}}%</span>
            
            </div>

            <div class="grains col-md-10">
                <h3>Grains & sucres</h3>
                <div class="row">
                    <div class="col-md-10" ng-repeat="fermentable in recipe.fermentables">
                        <div class="ing row">
                            <div class="col-md-6 ing-name"><span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="EBC : {{fermentable.color}} <br/> Rendement : {{fermentable.yield}}% <br/> Type : {{fermentable.type}} ">{{fermentable.name}}</span></div>
                            <div class="col-md-3 ing-amount">{{fermentable.amount}} g</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="hops col-md-10">
                <h3>Houblons</h3>
                <div class="row">
                    <div class="col-md-10" ng-repeat="hop in recipe.hops">
                        <div class="ing row">
                            <div class="col-md-3 ing-name">{{hop.name}}</div>
                            <div class="col-md-3 ing-amount">{{hop.amount}} g</div>
                            <div class="col-md-3 ing-amount">{{hop.time}} min ({{hop.use}})</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="hops col-md-10">
                <h3>Divers</h3>
                <div class="row">
                    <div class="col-md-10" ng-repeat="misc in recipe.miscs">
                        <div class="ing row">
                            <div class="col-md-3 ing-name">{{misc.name}}</div>
                            <div class="col-md-3 ing-amount">{{misc.amount}} g</div>
                            <div class="col-md-3 ing-amount">{{misc.time}} min ({{misc.use}})</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="yeasts col-md-10">
                <h3>Levures</h3>
                <div class="row">
                    <div class="col-md-7" ng-repeat="yeast in recipe.yeasts">
                        <div class="ing row">
                            <div class="col-md-6 ing-name">{{yeast.name}} {{yeast.labo}} {{yeast.product_id}}</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="yeasts profile col-md-10">
                <h3>Brassage</h3>
                <span class="profile-name">{{recipe.mashProfile.name}}</span>
                <span class="profile-ph">pH {{recipe.mashProfile.ph}}</span>
                <div ng-repeat="step in recipe.mashProfile.steps">
                    <p><span class="label-step">{{step.name}}</span> palier de type {{step.type}} à {{step.temp}} °C pendant {{step.time}} minutes</p>

                </div>
                <p><span class="label-step">Rinçage</span> {{recipe.mashProfile.sparge}} °C</p>
<!--                <div class="col-md-6" id="profile-graph" style="height:200px;"></div>-->
                  <linechart xkey="xkey" ykeys="ykeys" labels="labels" data="chartData"></linechart>
            </div>            

            <div class="yeasts notes col-md-10">
                <h3>Notes</h3>
                    <pre>{{recipe.notes}}</pre>            
            </div>    

            
        </div>

       
    <!-- Fin container     -->
    </div>





<script type="text/javascript">
new Morris.Line({
  element: 'profile-graph',
  axes:false,
  parseTime:true,
  postUnits: '°C',
  ymin:'45',
  data: [
    { y: '0 min', a: 66},
    { y: '60 min', a: 66},
    { y: '65 min', a: 78},
    { y: '75 min', a: 78}

  ],
  xkey: 'y',
  ykeys: ['a'],
  labels: ['Température'],
  xLabelMargin: 10,
});

</script> 
        

<script type="text/javascript">
                    $(function () {
                    $("[data-toggle='dropdown']").dropdown();
                    });
</script>

<script type="text/javascript">
    $(function () {
    $("[data-toggle='tooltip']").tooltip();
    });
</script>  

<script type="text/javascript">
                    $(function () {
                    $("[data-toggle='popover']").popover();
                    });
</script>          
</body>
</html>




''' 
    return resultHtml



