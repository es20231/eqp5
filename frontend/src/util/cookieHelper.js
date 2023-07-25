import Cookies from "js-cookie";

class CookieHelper {
    static setCookie(name, value, options = {}) {
        Cookies.set(name, value, options);
    }

    static getCookie(name) {
        return Cookies.get(name);
    }

    static deleteCookie(name) {
        Cookies.remove(name);
    }

    static checkCookie(name) {
        return Cookies.get(name) !== undefined;
    }
}

export default CookieHelper;