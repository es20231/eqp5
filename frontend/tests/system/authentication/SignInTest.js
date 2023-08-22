import { Builder, By, Key } from 'selenium-webdriver';
import { Options } from 'selenium-webdriver/chrome.js';

let options = new Options();
options.addArguments('-disable-dev-shm-usage');
let driver = new Builder().forBrowser('chrome').build();

async function run(){
    try{
        await driver.get('http://localhost:8080/');
        const email = await driver.findElement(By.xpath('//*[@id="exampleInputEmail"]'));
        await email.sendKeys('gleidesonfreitas015@gmail.com');
        await email.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const password = await driver.findElement(By.xpath('//*[@id="exampleInputPassword"]'));
        await password.sendKeys('roofroofattack08');
        await password.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const btnSignIn = await driver.findElement(By.xpath('//*[@id="app"]/div/div/div/div/div/form/button'));
        await btnSignIn.sendKeys(Key.ENTER);
    }finally{
        driver.quit();
    }
}

run();