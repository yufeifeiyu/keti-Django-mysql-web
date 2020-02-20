/*----------------------饼状图-----------------------*/
//环形图
var type = ['玄幻魔法', '武侠修真', '纯爱耽美', '都市言情', '职场校园', '穿越重生', '历史军事', '网游动漫', '恐怖灵异', '科幻小说', '美文名著'];

var data1 = {
    '玄幻魔法': [[2012, 2314], [2013, 2775], [2014, 2005], [2015, 5892], [2016, 801], [2017, 11407], [2018, 4243]]
    ,
    '武侠修真': [[2012, 724], [2013, 1221], [2014, 523], [2015, 1356], [2016, 219], [2017, 3057], [2018, 847]]
    ,
    '纯爱耽美': [[2012, 3], [2013, 1029], [2014, 141], [2015, 1055], [2016, 58], [2017, 595], [2018, 3045]]
    ,
    '都市言情': [[2012, 243], [2013, 1486], [2014, 2980], [2015, 6750], [2016, 1788], [2017, 15615], [2018, 6569]]
    ,
    '职场校园': [[2012, 560], [2013, 799], [2014, 561], [2015, 521], [2016, 25], [2017, 1064], [2018, 565]]
    ,
    '穿越重生': [[2012, 33], [2013, 248], [2014, 220], [2015, 1259], [2016, 67], [2017, 318], [2018, 72]]
    ,
    '历史军事': [[2012, 577], [2013, 899], [2014, 457], [2015, 2577], [2016, 1047], [2017, 11578], [2018, 4271]]
    ,
    '网游动漫': [[2012, 760], [2013, 1095], [2014, 266], [2015, 817], [2016, 126], [2017, 1439], [2018, 356]]
    ,
    '恐怖灵异': [[2012, 50], [2013, 137], [2014, 179], [2015, 564], [2016, 58], [2017, 276], [2018, 507]]
    ,
    '科幻小说': [[2012, 278], [2013, 639], [2014, 509], [2015, 792], [2016, 157], [2017, 4972], [2018, 1952]]
    ,
    '美文名著': [[2012, 2], [2013, 820], [2014, 1917], [2015, 3974], [2016, 2123], [2017, 9090], [2018, 2004]]
};
//alert(data1[type[0]][0][1]);

$("#select01").on("change", function () {

    year = $("#select01").val();

    year = year - 2012;

    $.get("", {
        "year": year,
    }, function (res) {
        obj = res


    }, 'json')

    var pie1 = echarts.init(document.getElementById("pie1"));

    option = {

        title: {
            text: year+2012+"年 "+"小说类型图",
            x: 'center'
        },

        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: type
        },
        series: [
            {
                name: '小说类型',
                type: 'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: [
                    {value: data1[type[0]][year][1], name: type[0]},
                    {value: data1[type[1]][year][1], name: type[1]},
                    {value: data1[type[2]][year][1], name: type[2]},
                    {value: data1[type[3]][year][1], name: type[3]},
                    {value: data1[type[4]][year][1], name: type[4]},
                    {value: data1[type[5]][year][1], name: type[5]},
                    {value: data1[type[6]][year][1], name: type[6]},
                    {value: data1[type[7]][year][1], name: type[7]},
                    {value: data1[type[8]][year][1], name: type[8]},
                    {value: data1[type[9]][year][1], name: type[9]},
                    {value: data1[type[10]][year][1], name: type[10]}
                ]
            }
        ]
    };

    pie1.setOption(option);

})
year = 6;
(function () {
    var pie1 = echarts.init(document.getElementById("pie1"));

    option = {

        title: {
            text: year+2012+"年 "+"小说类型图",
            x: 'center'
        },

        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: type
        },
        series: [
            {
                name: '小说类型',
                type: 'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: [
                    {value: data1[type[0]][year][1], name: type[0]},
                    {value: data1[type[1]][year][1], name: type[1]},
                    {value: data1[type[2]][year][1], name: type[2]},
                    {value: data1[type[3]][year][1], name: type[3]},
                    {value: data1[type[4]][year][1], name: type[4]},
                    {value: data1[type[5]][year][1], name: type[5]},
                    {value: data1[type[6]][year][1], name: type[6]},
                    {value: data1[type[7]][year][1], name: type[7]},
                    {value: data1[type[8]][year][1], name: type[8]},
                    {value: data1[type[9]][year][1], name: type[9]},
                    {value: data1[type[10]][year][1], name: type[10]}
                ]
            }
        ]
    };

    pie1.setOption(option);
})();


//嵌套环形图
(function () {

    var pie2 = echarts.init(document.getElementById("pie2"));

    option = {

        title: {
            text: "环形图",
            x: 'center'
        },

        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: ['直达', '营销广告', '搜索引擎', '邮件营销', '联盟广告', '视频广告', '百度', '谷歌', '必应', '其他']
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                selectedMode: 'single',
                radius: [0, '30%'],

                label: {
                    normal: {
                        position: 'inner'
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: [
                    {value: 335, name: '直达', selected: true},
                    {value: 679, name: '营销广告'},
                    {value: 1548, name: '搜索引擎'}
                ]
            },
            {
                name: '访问来源',
                type: 'pie',
                radius: ['40%', '55%'],

                data: [
                    {value: 335, name: '直达'},
                    {value: 310, name: '邮件营销'},
                    {value: 234, name: '联盟广告'},
                    {value: 135, name: '视频广告'},
                    {value: 1048, name: '百度'},
                    {value: 251, name: '谷歌'},
                    {value: 147, name: '必应'},
                    {value: 102, name: '其他'}
                ]
            }
        ]
    };
    pie2.setOption(option);
})();


//饼状图
(function () {

    var pie3 = echarts.init(document.getElementById("pie3"));

    option = {
        title: {
            text: '某站点用户访问来源',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: [
                    {value: 335, name: '直接访问'},
                    {value: 310, name: '邮件营销'},
                    {value: 234, name: '联盟广告'},
                    {value: 135, name: '视频广告'},
                    {value: 1548, name: '搜索引擎'}
                ],
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    pie3.setOption(option);
})();


//南丁格尔玫瑰图
(function () {

    var pie4 = echarts.init(document.getElementById("pie4"));

    option = {
        title: {
            text: '南丁格尔玫瑰图',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x: 'center',
            y: 'bottom',
            data: ['rose1', 'rose2', 'rose3', 'rose4', 'rose5', 'rose6', 'rose7', 'rose8']
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {
                    show: true,
                    type: ['pie', 'funnel']
                },
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        series: [
            {
                name: '半径模式',
                type: 'pie',
                radius: [20, 110],
                center: ['25%', '50%'],
                roseType: 'radius',
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                lableLine: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [
                    {value: 10, name: 'rose1'},
                    {value: 5, name: 'rose2'},
                    {value: 15, name: 'rose3'},
                    {value: 25, name: 'rose4'},
                    {value: 20, name: 'rose5'},
                    {value: 35, name: 'rose6'},
                    {value: 30, name: 'rose7'},
                    {value: 40, name: 'rose8'}
                ]
            },
            {
                name: '面积模式',
                type: 'pie',
                radius: [30, 110],
                center: ['75%', '50%'],
                roseType: 'area',
                data: [
                    {value: 10, name: 'rose1'},
                    {value: 5, name: 'rose2'},
                    {value: 15, name: 'rose3'},
                    {value: 25, name: 'rose4'},
                    {value: 20, name: 'rose5'},
                    {value: 35, name: 'rose6'},
                    {value: 30, name: 'rose7'},
                    {value: 40, name: 'rose8'}
                ]
            }
        ]
    };

    pie4.setOption(option);
})();