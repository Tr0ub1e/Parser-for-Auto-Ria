from bs4 import BeautifulSoup
import requests



def main():

    data = []
    headers = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9) Gecko/2008052906 Firefox/3.0'}

    for pages in range(125):

        url = "https://auto.ria.com/search/?body.id[0]=3&body.id[3]=4&body.id[5]=6&year[0].gte=1990&categories.main.id=1&price.USD.lte=3000&price.currency=1&gearbox.id[0]=1&abroad.not=0&custom.not=1&page="+str(pages)+"&size=100"
        req = requests.get(url, headers=headers)
        print(url)
        print(req.status_code)
        soup = BeautifulSoup(req.text, 'html.parser')

        for i in range(100):

            name = soup.find_all(class_='item ticket-title')[i].get_text()
            price = soup.find_all(class_='bold green size22', attrs={"data-currency":"USD"})[i].get_text()

            add_data = soup.find_all(class_='unstyle characteristic')[i].get_text()
            add_data = add_data.split()

            data.append([name, price, add_data[0], add_data[5]])

            with open('data.csv', 'a') as file:
                for i in data:

                    i = str(i)
                    i = i.replace(" ", "")
                    i = i.replace("\'", "")
                    i = i.replace('[', '')
                    i = i.replace(']', '')
                    file.write(i + '\n')

        print(pages, req.status_code)

    print('Готово')
    input()

if __name__ == '__main__':
    main()
