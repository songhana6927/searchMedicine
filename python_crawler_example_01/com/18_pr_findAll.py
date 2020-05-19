from bs4 import BeautifulSoup

html = """
    <html>
        <table>
            <tr>
                <td class='first'>100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>
        </table>
    </html>
"""

bs_obj = BeautifulSoup(html,"html.parser")

#100
td_first = bs_obj.find("td",{"class","first"})
#print(td_first)

#200
table = bs_obj.find("table")
tr = bs_obj.find("tr")
tds = tr.findAll("td")
#print(tds[1].text)

#300
table = bs_obj.find("table")
trs = bs_obj.findAll("tr")
tds = trs[1].findAll("td")
print(tds[0].text)
