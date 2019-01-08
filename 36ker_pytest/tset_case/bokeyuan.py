from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.cnblogs.com/")



cookie_1 = {
        "name": "CNBlogsCookie",
        "value": "799C71F3513B9C2DFFE10A38E7BB691AB9A594C4BA81EA760AE535C23C9AA8AC60FAC7C48C4121A13F5B1686BE9777EC749A08DABAE7917025017B7CF15FE776048A83B35119EC74BED563035AAB6DA19C13E95D",
          }
cookie_2 = {
    'name': 'Cnblogs.AspNetCore.Cookies',
    'value': "CfDJ8KlpyPucjmhMuZTmH8oiYTN3XkoB4JpvLqwVABdSdOrzu9b5Fr_CN79ydy71aXrLwzrp2VrBFHo_Yn6cTbkV5Cdw8aFdPJHp_e4-7prwt0L7aKfQOpQD9lmTgFaQRMJLBEdflTzyEDXVMVKrb-cAI9xu4JqWWJkMv3yQz9Py2Edmhfy-8HAu6bkK696DsvhpwMkqlrjXhzgrPdjK6ZtTgQac1p33q5hsvrXRcvvaMUNHVEMPvLrK6pqnzeZUEJxSs5CB8qcXTRSNZh-r4KfZXi4maw567zUAvlr7zsNTr15z"
}
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
driver.refresh()