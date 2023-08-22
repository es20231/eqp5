import { Builder, By, Key } from 'selenium-webdriver';
import { Options } from 'selenium-webdriver/chrome.js';

let options = new Options();
options.addArguments('-disable-dev-shm-usage');
let driver = new Builder().forBrowser('chrome').build();

async function run(){
    try{
        await driver.get('http://localhost:8080/');
        const email = await driver.findElement(By.xpath('//*[@id="exampleInputEmail"]'));
        await email.sendKeys('zedamanga@manga.com');
        await email.sendKeys(Key.TAB);
        await driver.sleep(1000);
        const password = await driver.findElement(By.xpath('//*[@id="exampleInputPassword"]'));
        await password.sendKeys('roofroofattack08');
        await password.sendKeys(Key.TAB);
        await driver.sleep(1000);
        const click = await driver.findElement(By.xpath('//*[@id="app"]/div/div/div/div/div/form/button'));
        await click.sendKeys(Key.ENTER);
        await driver.sleep(1000);
        const btnLogOut = await driver.findElement(By.xpath('//*[@id="wrapper"]/div[1]/li[3]/a'));
        await btnLogOut.sendKeys(Key.ENTER);
        await driver.sleep(1000);
    }finally{
        driver.quit();
    }
}
run();