#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : Liqc
@Date    : 2024/1/30
@Version : v1.0.0
@Description: 响应文件
"""
from flask import Flask, Response, send_file
import requests

app = Flask(__name__)


def main():
    """
    下载文件功能接口
    """
    @app.route('/file/123', methods=['post', 'get'])
    def chat():
        # response 响应 assets/123.xlsx 文件
        # return Response(response, content_type='text/event-stream; charset=utf-8')

        return send_file('assets/123.xlsx')
    app.run(port=8856, host='0.0.0.0')


if __name__ == '__main__':
    main()


