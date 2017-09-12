# encoding:utf-8 
from bs4 import BeautifulSoup
from lxml import etree
page_source= '''
<div class="exrt">
        <!--二级导航-->
        <div class="mt">
    <ul class="mt_l">
        <li class="on"><a href="http://i.51job.com/userset/my_apply.php?type=sh&amp;lang=c">社会申请</a> <span>921</span></li>
                    </ul>
        <ul class="mt_r" style="display: block;">
        <li>保留近60天的社会申请记录，超出期限数据会自动更新</li>
    </ul>
    </div>
        <!--社会申请 不为空-->
                    <div class="exmsg" style="display:block">
                <div class="rbox">
                    <div class="tit">
                        <ul class="clearfix">
                            <li class="l4">职位名</li>
                            <li class="l9">公司名</li>
                            <li class="l6">工作地点</li>
                            <li class="l10">薪资</li>
                            <li class="l11">申请日期</li>
                        </ul>
                    </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="Web前端开发工程师" href="http://jobs.51job.com/all/82400149.html?s=02&amp;t=0">
                                        Web前端开发工程师                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海欣导文化传媒有限公司" href="http://jobs.51job.com/all/co4097509.html">
                                        上海欣导文化传媒有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">5-8千/月</li>
                                <li class="l11">2017-04-08</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>python </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">0</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9156987198,1491634849,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="web前端工程师" href="http://jobs.51job.com/all/87688118.html?s=02&amp;t=0">
                                        web前端工程师                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海超越极限教育科技有限公司" href="http://jobs.51job.com/all/co3986596.html">
                                        上海超越极限教育科技有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">1.2-2万/月</li>
                                <li class="l11">2017-04-08</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>python </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">102</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9156973086,1491634523,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="策略交易开发" href="http://jobs.51job.com/all/86506980.html?s=02&amp;t=0">
                                        策略交易开发                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海吉贝克信息技术有限公司" href="http://jobs.51job.com/all/co1204119.html">
                                        上海吉贝克信息技术有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">1.5-2万/月</li>
                                <li class="l11">2017-04-01</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>期货2 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">18</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9127234754,1490999110,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="策略研究员" href="http://jobs.51job.com/all/83555335.html?s=02&amp;t=0">
                                        策略研究员                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海弘润资产管理有限责任公司" href="http://jobs.51job.com/all/co4109139.html">
                                        上海弘润资产管理有限责任公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">1-3万/月</li>
                                <li class="l11">2017-04-01</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>期货2 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">30</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9127234621,1490999091,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="高级策略师" href="http://jobs.51job.com/all/68807128.html?s=02&amp;t=0">
                                        高级策略师                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="西南期货有限公司" href="http://jobs.51job.com/all/co3634255.html">
                                        西南期货有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">2-2.5万/月</li>
                                <li class="l11">2017-04-01</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>期货2 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">0</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9127234379,1490999049,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="期货IT编程程序员" href="http://jobs.51job.com/all/87697735.html?s=02&amp;t=0">
                                        期货IT编程程序员                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海善能资产管理中心（有限合伙）" href="http://jobs.51job.com/all/co4227871.html">
                                        上海善能资产管理中心（有限合伙）                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">5-6千/月</li>
                                <li class="l11">2017-04-01</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>期货2 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">0</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9127234144,1490998997,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化程序员" href="http://jobs.51job.com/all/86533288.html?s=02&amp;t=0">
                                        量化程序员                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海璨龙资产管理有限公司" href="http://jobs.51job.com/all/co4289526.html">
                                        上海璨龙资产管理有限公司                                    </a>
                                </li>
                                <li class="l6"></li>
                                <li class="l10 c_orange">&nbsp;</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">1</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122054948,1490875864,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="机器学习岗" href="http://jobs.51job.com/all/86132184.html?s=02&amp;t=0">
                                        机器学习岗                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海金融期货信息技术有限公司" href="http://jobs.51job.com/all/co2926038.html">
                                        上海金融期货信息技术有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">20-35万/年</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">6</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122052821,1490875826,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化策略研究员" href="http://jobs.51job.com/all/83629306.html?s=02&amp;t=0">
                                        量化策略研究员                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海茂典资产管理有限公司" href="http://jobs.51job.com/all/co4138326.html">
                                        上海茂典资产管理有限公司                                    </a>
                                </li>
                                <li class="l6">上海-黄浦区</li>
                                <li class="l10 c_orange">2-2.5万/月</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">39</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122049608,1490875769,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化投资/研究员(上海)" href="http://nesc.51job.com/sc/show_job_detail.php?jobid=84892521">
                                        量化投资/研究员(上海)                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="东北证券股份有限公司" href="http://nesc.51job.com">
                                        东北证券股份有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">&nbsp;</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>python </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">26</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122048341,1490875747,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化研究岗" href="http://jobs.51job.com/all/80635630.html?s=02&amp;t=0">
                                        量化研究岗                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="国海良时期货有限公司" href="http://jobs.51job.com/all/co2276685.html">
                                        国海良时期货有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">8-12万/年</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">56</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122041106,1490875623,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化投资经理（资产管理部）" href="http://jobs.51job.com/all/86808861.html?s=02&amp;t=0">
                                        量化投资经理（资产管理部）                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海中期期货有限公司" href="http://jobs.51job.com/all/co2117988.html">
                                        上海中期期货有限公司                                    </a>
                                </li>
                                <li class="l6">上海</li>
                                <li class="l10 c_orange">1-1.5万/月</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">24</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122038944,1490875592,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="量化策略研究员" href="http://jobs.51job.com/all/85024629.html?s=02&amp;t=0">
                                        量化策略研究员                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="比诺供应链管理（上海）有限公司" href="http://jobs.51job.com/all/co3654054.html">
                                        比诺供应链管理（上海）有限公司                                    </a>
                                </li>
                                <li class="l6">上海-杨浦区</li>
                                <li class="l10 c_orange">1-1.5万/月</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">21</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122034910,1490875525,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="初级量化分析师" href="http://jobs.51job.com/all/87488797.html?s=02&amp;t=0">
                                        初级量化分析师                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="上海引翎者商贸有限公司" href="http://jobs.51job.com/all/co3763909.html">
                                        上海引翎者商贸有限公司                                    </a>
                                </li>
                                <li class="l6">上海-浦东新区</li>
                                <li class="l10 c_orange">0.7-1万/月</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">1</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122030517,1490875451,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                            <div class="rli">
                            <ul class="clearfix">
                                <li class="l4 dt">
                                    <a target="_blank" title="python工程师" href="http://jobs.51job.com/all/85105169.html?s=02&amp;t=0">
                                        python工程师                                    </a>
                                                                    </li>
                                <li class="l9">
                                    <a target="_blank" title="齐数科技（上海）有限公司" href="http://jobs.51job.com/all/co3341502.html">
                                        齐数科技（上海）有限公司                                    </a>
                                </li>
                                <li class="l6">上海-徐汇区</li>
                                <li class="l10 c_orange">1-1.5万/月</li>
                                <li class="l11">2017-03-30</li>
                            </ul>
                            <div class="rsp">
                                <ul class="clearfix">
                                    <li class="l8">申请：<span>其他 </span> </li>
                                                                            <li class="l8">近两周申请：<span class="c_green">11</span>人</li>
                                                                                                                    <li class="l12">&nbsp;<span class="c_green">&nbsp;</span></li>
                                        <li class="l10"><a class="a" href="javascript:void(0);" onclick="showLayer()">竞争力分析</a></li>
                                                                                                                <li class="l11" onclick="progress(this,9122022505,1490875317,1);"><span class="view">查看进度<em></em></span></li>
                                                                    </ul>
                            </div>
                            <div class="rate" style="display: none;">
                            </div>
                        </div>
                                    </div>
                <!--分页-->
                <div class="dw_page">
                    <div class="p_box">
                        <div class="p_wp">
                            <div class="p_in">
                                <ul>
                                    <!-- 上一页 -->
                                                                            <li class="bk"><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=60">上一页</a></li>
                                                                        <!--数字页码-->
                                                                                                                        <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=56">56</a></li>
                                                                                                                                                                <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=57">57</a></li>
                                                                                                                                                                <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=58">58</a></li>
                                                                                                                                                                <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=59">59</a></li>
                                                                                                                                                                <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=60">60</a></li>
                                                                                                                                                                <li class="on">61</li>
                                                                                                                                                                    <li><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=62">62</a></li>
                                                                                                                <!-- 下一页 -->
                                                                            <li class="bk"><a href="http://i.51job.com/userset/my_apply.php?lang=c&amp;type=sh&amp;page=62">下一页</a></li>
                                                                    </ul>
                                <span class="td">共62页，到第</span>
                                <input id="jump_page" class="mytxt" value="61" type="text">
                                <span class="td">页</span>
                                <span class="og_but" onclick="jump_page();">确定</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
                </div>

'''

soup = BeautifulSoup(page_source, 'lxml')
alla = soup.find_all('li')
#print alla

selector = etree.HTML(page_source)
#print etree.tostring(selector)
rli = selector.xpath('//div[@class="rli"]')

all_apply = []
#for i, one in enumerate(rli):
#    print type(one), one
#    print one.xpath('//div[@class="rate"]/div[@class="now"]/em/text()')
#    #print one.xpath
#    one_apply = dict.fromkeys(['job','company', 'place', 'salary', 'apply_date', 'resume_name', 'recent_apply', 'rate'])
#    one_apply['job'] = one.xpath('//li[1]/a/text()')[i+1].strip()
#    one_apply['company'] = one.xpath('//li[2]/a/text()')[i+1].strip()
#    one_apply['place'] = one.xpath('//li[3]/text()')[i+1].strip()
#    one_apply['salary'] = one.xpath('//li[4]/text()')[i+1].strip()
#    one_apply['apply_date'] = one.xpath('//li[5]/text()')[i+1].strip()
#    one_apply['resume_name'] = one.xpath('//div[@class="rsp"]/ul/li[1]/span/text()')[i].strip()
#    one_apply['recent_apply'] = one.xpath('//div[@class="rsp"]/ul/li[2]/span/text()')[i].strip()
#    one_apply['rate'] = one.xpath('//div[@class="rate"]/div[@class="now"]/em/text()')[i].strip()
#    all_apply.append(one_apply)
jobs = selector.xpath('//div[@class="rli"]/ul/li[1]/a/text()') # 要strip
companies = selector.xpath('//div[@class="rli"]/ul/li[2]/a/text()') # 要strip
places = selector.xpath('//div[@class="rli"]/ul/li[3]/text()')
salaries = selector.xpath('//div[@class="rli"]/ul/li[4]/text()')
apply_dates = selector.xpath('//div[@class="rli"]/ul/li[5]/text()')
resume_names = selector.xpath('//div[@class="rsp"]/ul/li[1]/span/text()')
recent_applies = selector.xpath('//div[@class="rsp"]/ul/li[2]/span/text()')
rates = selector.xpath('//div[@class="rate"]/div/em/text()')
#print jobs
print type(rates)
for n in rates:
    print type(n), n


print range(1,9)

import sys
import os
print sys.path
sys.path.append('..')
print sys.path
