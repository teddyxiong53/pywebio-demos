from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info



def main():
    info = input_group(
        'bmi计算',
        [
        input('请输入你的身高', name='height', type=FLOAT),
        input('请输入你的体重', name='weight', type=FLOAT),
        ]
    )
    print(session_info.user_language)
    put_html(f'身高{info["height"]} 体重{info["weight"]}')

if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
