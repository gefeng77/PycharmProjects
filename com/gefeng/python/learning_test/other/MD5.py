# coding=utf-8
import hashlib


def sign_body(body, apiKey="12345678"):
    a = ["=".join(i) for i in body.items() if i[0] != "Sign"]
    # print(a)

    # 参数名按ASCII码从小到大排列
    strA = ",".join(sorted(a))
    # print(strA)
    strSignTemp = strA + ",apiKey=12345678"
    print(strSignTemp)

    def md5(src):
        m = hashlib.md5()
        m.update(src.encode("utf-8"))
        return m.hexdigest()

    sign = md5(strSignTemp.lower())
    # print(sign)

    body["Sign"] = sign
    # print(body)
    return body


if __name__ == "__main__":
    apiKey = "12345678"

    body = {
        "Username": "learning_test",
        "Password": "123456",
        "Mail": "gefeng_zhang@outlook.com",
        "Sign": ""
    }
    print(sign_body(body, apiKey="12345678"))
