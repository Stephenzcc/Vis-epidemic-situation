let ec_right1 = echarts.init(document.getElementById('r1'), 'dark');
let ec_right1_option = {
	title: {
		show: true,
		text: '非湖北地区确诊TOP5',
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            data: [],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            type: 'bar',
            barMaxWidth: '60%',
            data: []
        }
    ]
};