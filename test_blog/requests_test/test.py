from requests_test.selenu_auto import runCase

if __name__ == '__main__':
    data = {"exeItems": [{"itemName": "test_eq", "itemDesc": "//div[2]/div/div[1]/div/div[1]/div/div[1]/div/a", "action": "click", "expectation": "an expect page info."}]}
    runCase('http://www.jiafanblog.com').parse(data)

    data2 = [{
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
                "name": "test_index_essaycount",
                "err_msg": "文章条数统计有误",
                "image_url": './image/test_index_essaycount.png',
                "xpath_name": "count"
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
