from requests_test.case import RunCase

if __name__ == '__main__':
    RunCase()
    data2 = [
        {
        "config": {
            "name": "case01",
            "variables": [],
            "request": {
                "base_url": "http://www.jiafanblog.com",
                "headers": {}
            }
        }
    },
        {
            "test": {
                "name": "test_index_info",
                "err_msg": "没有跳转到个人页面",
                "image_url": './image/test_index_info.png',
                "xpath_name": "user_info"
            }
        },
        {
            "test": {
                "name": "test_index_free",
                "err_msg":"没有跳转到分类",
                "image_url": './image/test_index_free.png',
                "xpath_name": "free"
            }
        },
        {
            "test": {
                "name": "test_index_image",
                "err_msg": "跳转到详情页错误",
                "image_url": './image/test_index_image.png',
                "xpath_name": "start_image_details"
            }
        },
        {
            "test": {
                "name": "test_index_essaycount",
                "err_msg": "文章条数统计有误",
                "image_url":  './image/test_index_essaycount.png',
                "xpath_name": "count"
            }
            }

    ]

