from config import charts_demo_host
from pywebio.output import put_markdown, put_row, put_html
from pywebio.session import info as session_info

index_md = r"""
# 练习
- [BMI 计算](./bmi): 计算 bmi

"""

def main():
    put_row([
        put_markdown('# 汉良软件（HLSOFT）'),
    ])

    put_markdown(index_md)
