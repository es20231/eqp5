import { Builder, By, Key } from 'selenium-webdriver';
import { Options } from 'selenium-webdriver/chrome.js';

let options = new Options();
options.addArguments('-disable-dev-shm-usage');
let driver = new Builder().forBrowser('chrome').build();


async function run(){
    try{
        await driver.get('http://localhost:8080/');
        const click = await driver.findElement(By.xpath('//*[@id="app"]/div/div/div/div/div/div[2]/div[2]/a'));
        await click.sendKeys(Key.ENTER);
        await driver.sleep(2000);
        const username = await driver.findElement(By.xpath('//*[@id="exampleInputUsername"]'));
        await username.sendKeys('juvenalDaG');
        await username.sendKeys(Key.TAB);
        await driver.sleep(2000);
        
        const name = await driver.findElement(By.xpath('//*[@id="exampleInputFullName"]'));
        await name.sendKeys('Juneval da Genoveva');
        await name.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const email = await driver.findElement(By.xpath('//*[@id="exampleInputEmail"]'));
        await email.sendKeys('gleidesonfreitas015@gmail.com');
        await email.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const password = await driver.findElement(By.xpath('//*[@id="exampleInputPassword"]'));
        await password.sendKeys('roofroofattack08');
        await password.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const confirmPassword = await driver.findElement(By.xpath('//*[@id="exampleInputConfirmPassword"]'));
        await confirmPassword.sendKeys('roofroofattack08');
        await confirmPassword.sendKeys(Key.TAB);
        await driver.sleep(2000);
        const btnSignUp = await driver.findElement(By.xpath('//*[@id="app"]/div/div/div/div/div/form/button'));
        await btnSignUp.sendKeys(Key.ENTER);

    }finally{
        driver.quit();
    }
}
run();