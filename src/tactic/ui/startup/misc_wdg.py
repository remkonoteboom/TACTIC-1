###########################################################
#
# Copyright (c) 2010, Southpaw Technology
#                     All Rights Reserved
#
# PROPRIETARY INFORMATION.  This software is proprietary to
# Southpaw Technology, and is not to be reproduced, transmitted,
# or disclosed in any way without written permission.
#
#

__all__ = ['TitleWdg', 'QuickLinksWdg', 'MainShelfWdg', 'BubbleWdg']

from pyasm.common import Environment, Common
from pyasm.search import Search
from pyasm.biz import Project
from pyasm.web import DivWdg, HtmlElement, SpanWdg, Table, Widget
from pyasm.widget import IconWdg, TextWdg

import os

from tactic.ui.common import BaseRefreshWdg
from tactic.ui.widget import ActionButtonWdg, IconButtonWdg, SingleButtonWdg




class TitleWdg(BaseRefreshWdg):

    def get_display(self):
        top = self.top

        title = self.kwargs.get("title")

        title_wdg = DivWdg()
        top.add(title_wdg)
        title_wdg.add(title)
        title_wdg.add_style("font-size: 18px")
        title_wdg.add_style("font-weight: bold")
        title_wdg.add_style("text-align: center")
        title_wdg.add_style("padding: 10px")
        title_wdg.add_style("margin: -10px -10px 10px -10px")
        title_wdg.add_gradient("background", "background3", 5, -10)

        return top




class BubbleWdg(BaseRefreshWdg):

    def get_display(self):

        msg = self.kwargs.get("message")

        arrow_div = DivWdg()
        icon = IconWdg(msg, IconWdg.ARROW_UP_LEFT_32)
        icon.add_style("margin-top: -20")
        icon.add_style("margin-left: -15")
        icon.add_style("position: absolute")
        arrow_div.add(icon)
        arrow_div.add("&nbsp;"*5)
        arrow_div.add("<b>%s</b>" % msg)
        arrow_div.add_style("position: relative")
        arrow_div.add_style("margin-top: 5px")
        arrow_div.add_style("margin-left: 20px")
        arrow_div.add_style("float: left")
        arrow_div.add_style("padding: 25px")
        arrow_div.set_box_shadow("1px 1px 2px 2px")
        arrow_div.set_round_corners(30)
        arrow_div.add_color("background", "background")
        return arrow_div



class QuickLinksWdg(BaseRefreshWdg):

    def get_args_keys(self):
        return {
        }


    def get_display(self):


        top = DivWdg()
        title = DivWdg()

        top.add(title)
        top.add_color("background", "background")
        top.add_style("margin: 0px 10px 15px 10px")
        #top.set_box_shadow()

        title.add("More Information")
        title.add_style("font-size: 16px")
        title.add_style("padding: 5px")
        title.add_color("background", "background", -5)
        title.add_border()
        #title.set_round_corners(corners=['TL','TR'])

        content_wdg = DivWdg()
        top.add(content_wdg)
        content_wdg.add_border()
        content_wdg.add_style("padding: 20px")

        content_wdg.add("<div style='font-size: 12px'>The following links will help you find out more information on how to set-up or use TACTIC.</div>")
        content_wdg.add("<hr/>")

        hover = title.get_color("background", -10)


        links_div = DivWdg()
        links_div.add_style("padding: 10px")
        content_wdg.add(links_div)


        # documentation linke
        link_div = DivWdg()
        link_div.add_style("padding-left: 10px")
        links_div.add(link_div)


        #icon = IconWdg("Documentation", IconWdg.DOCUMENTATION)
        icon = IconWdg("Documentation", "FAS_BOOK", size=16)

        icon.set_box_shadow("2px 2px 5px")
        icon.add_border()
        icon.add_style("padding: 5px 3px 5px 3px")
        icon.set_round_corners()
        #icon.add_color("background", "background3")
        icon.add_style("width: 32")
        icon.add_style("display: inline-block")
        icon.add_style("text-align: center")

        link_div.add(icon)
        link_div.add("&nbsp;"*2)

        link = HtmlElement.href("Documentation", "/doc/", target="_blank")
        link_div.add_behavior( {
            'type': 'click_up',
            'cbjs_action': '''
            spt.help.set_top();
            spt.help.load_alias("main");
            '''
        } )

        link_div.add_behavior( {
        'type': 'hover',
        'color': hover,
        'cbjs_action_over': '''
        bvr.src_el.setStyle("background", bvr.color);
        ''',
        'cbjs_action_out': '''
        bvr.src_el.setStyle("background", "");
        '''
        } )
        link_div.add(link)
        link.add_color("color", "color")

        links_div.add("<br/>")



        link_div = DivWdg()
        link_div.add_style("padding-left: 10px")
        links_div.add(link_div)

        #icon = IconWdg("Community", IconWdg.COMMUNITY)
        icon = IconWdg("Community", "FAS_USERS", size=16)

        icon.set_box_shadow("2px 2px 5px")
        icon.add_border()
        icon.add_style("padding: 5px 3px 5px 3px")
        icon.set_round_corners()
        #icon.add_color("background", "background3")

        link_div.add(icon)
        link_div.add("&nbsp;"*2)
        link = HtmlElement.href("Community", "http://community.southpawtech.com", target="_blank")
        link_div.add(link)
        link.add_color("color", "color")
        link_div.add_behavior( {
        'type': 'hover',
        'color': hover,
        'cbjs_action_over': '''
        bvr.src_el.setStyle("background", bvr.color);
        ''',
        'cbjs_action_out': '''
        bvr.src_el.setStyle("background", "");
        '''
        } )

        links_div.add("<br/>")

        # documentation link
        link_div = DivWdg()
        link_div.add_style("padding-left: 10px")
        links_div.add(link_div)

        #icon = IconWdg("Support", IconWdg.WEBSITE)
        icon = IconWdg("Support", "FAS_PHONE")

        icon.set_box_shadow("2px 2px 5px")
        icon.add_border()
        icon.add_style("padding: 5px 3px 5px 3px")
        icon.add_style("width: 30px")
        icon.add_style("display: inline-block")
        icon.set_round_corners()
        #icon.add_color("background", "background3")


        link_div.add(icon)
        link_div.add("&nbsp;"*2)

        link = HtmlElement.href("Support", "http://www.southpawtech.com", target="_blank")
        link_div.add(link)
        link.add_color("color", "color")
        link_div.add_behavior( {
        'type': 'hover',
        'color': hover,
        'cbjs_action_over': '''
        bvr.src_el.setStyle("background", bvr.color);
        ''',
        'cbjs_action_out': '''
        bvr.src_el.setStyle("background", "");
        '''
        } )



        return top




class MainShelfWdg(BaseRefreshWdg):

    def get_display(self):

        top = self.top

        button_div = DivWdg()
        top.add(button_div)
        button_div.add_class("spt_buttons_top")
        button_div.add_border()


        button_div.add_style("margin-bottom: 0px")
        button_div.add_style("width: 100%")
        button_div.add_style("height: 50px")
        button_div.add_color("background", "background2")
        button_div.add_style("margin-left: auto")
        button_div.add_style("margin-right: auto")

        button_div.add_style("display: flex")
        button_div.add_style("align-items: center")

        button = SingleButtonWdg(title="Collapse", icon="FA_HOME")
        button_div.add(button)
        button.add_style("margin-left: 15px")


        # FIXME: get home for the user
        #home = 'tactic.ui.startup.ContentCreatorWdg'
        home = 'tactic.ui.startup.MainWdg'


        button.add_behavior( {
            'type': 'click_up',
            'cbjs_action': '''
            spt.tab.set_main_body_tab();
            var class_name = 'tactic.ui.startup.MainWdg';
            var kwargs = {
                help_alias: 'main'
                };
            spt.tab.add_new("_startup", "Startup", class_name, kwargs);

            '''
        } )


        top_class = self.kwargs.get("top_class")
        list_class = self.kwargs.get("list_class")
        height = self.kwargs.get("height")
        assert(top_class)
        assert(list_class)
        assert(height)

        button = SingleButtonWdg(title="Collapse", icon="FA_ARROW_UP")
        button_div.add(button)
        button.add_class("spt_collapse")
        top.add(button_div)
        button.add_style("margin-left: 5px")

        button.add_behavior( {
            'type': 'click_up',
            'top_class': top_class,
            'list_class': list_class,
            'height': height,
            'cbjs_action': '''
            var top = bvr.src_el.getParent("."+bvr.top_class);
            var element = top.getElement("."+bvr.list_class);

            var buttons = bvr.src_el.getParent(".spt_buttons_top");
            expand = buttons.getElement(".spt_expand");
            new Fx.Tween(element).start('margin-top', "-"+bvr.height+"px");
            expand.setStyle("display", "");
            bvr.src_el.setStyle("display", "none");
            '''
        } )

        button = SingleButtonWdg(title="Expand", icon="FA_ARROW_DOWN")
        button.add_style("display: none")
        button.add_class("spt_expand")
        button_div.add(button)
        button.add_style("margin-left: 15px")
        top.add(button_div)
        button.add_behavior( {
            'type': 'click_up',
            'top_class': top_class,
            'list_class': list_class,
            'cbjs_action': '''
            var top = bvr.src_el.getParent("."+bvr.top_class);
            var element = top.getElement("."+bvr.list_class);

            var buttons = bvr.src_el.getParent(".spt_buttons_top");
            collapse = buttons.getElement(".spt_collapse");
            new Fx.Tween(element).start('margin-top', "0px");
            collapse.setStyle("display", "");
            bvr.src_el.setStyle("display", "none");
            '''
        } )

        return top



