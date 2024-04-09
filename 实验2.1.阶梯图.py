from pyecharts.charts import Line
import pyecharts.options as opts

line = (
    Line()
    .add_xaxis(["1995", "1996", "1997", "1998", "1999", "2000",
          "2001", "2002", "2003", "2004", "2005", "2006",
          "2007", "2008", "2009"])
    .add_yaxis("1995-2009年美国邮票价格",
               [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37,
                0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44],
               is_step=True)
    .set_global_opts(
        title_opts=opts.TitleOpts(title='阶梯图'),
        yaxis_opts=opts.AxisOpts(min_=0.2, max_=0.5)  # 设置 y 坐标轴刻度最小值和最大值
    )
)
line.render("阶梯图.html")
