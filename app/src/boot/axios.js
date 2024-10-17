import { boot } from 'quasar/wrappers';
import { Notify } from 'quasar';
import axios from 'axios';

class UInstance {
  // eslint-disable-next-line default-param-last
  constructor(baseURL, config = {}, store) {
    config.baseURL = baseURL;
    this.instance = axios.create(config);
    this.store = store;
    this.config = config;
    this.token = undefined;
  }

  static handleMessages(response) {
    const { data } = response;

    if (data.INFORMATIONS && data.INFORMATIONS.length > 0) {
      data.INFORMATIONS.forEach((message) => {
        Notify.create({
          color: 'positive',
          textColor: 'white',
          // eslint-disable-next-line object-shorthand
          message: message,
        });
      });
    }

    if (data.ERRORS && data.ERRORS.length > 0) {
      data.ERRORS.forEach((message) => {
        Notify.create({
          color: 'red-5',
          textColor: 'white',
          icon: 'warning',
          // eslint-disable-next-line object-shorthand
          message: message,
        });
      });
    }
  }

  static handleResponse(promise, silent) {
    // eslint-disable-next-line no-async-promise-executor
    return new Promise(async (resolve, reject) => {
      try {
        const response = await promise;

        if (!silent) {
          UInstance.handleMessages(response);
        }

        const { data } = response;

        if (data instanceof Blob) {
          resolve(data);
          return;
        }

        resolve(data.data);
      } catch (e) {
        if (e && e.data) {
          // UInstance.handleMessages(e.response);
        }

        reject(e);
      }
    });
  }

  static serialize(param, returnFormData) {
    if (returnFormData) {
      const formData = new FormData();
      Object.keys(param).forEach((key) => {
        if (param[key] !== null && param[key] !== undefined) formData.append(key, param[key]);
      });

      return formData;
    }
    let params = '';
    // eslint-disable-next-line no-restricted-syntax
    for (const key in param) {
      // eslint-disable-next-line no-prototype-builtins
      if (param.hasOwnProperty(key)) {
        if (param[key] !== undefined && param[key] !== null) {
          if (params.length > 0) {
            params += '&';
          }
          params += `${key}=${encodeURIComponent(param[key])}`;
        }
      }
    }

    return params;
  }

  getURL(url, query) {
    url = this.config.baseURL + url;

    if (!query) {
      query = {};
    }

    if (query) {
      url += `?${UInstance.serialize(query)}`;
    }

    return url;
  }

  get(url, query, config) {
    if (query) {
      url += `?${UInstance.serialize(query)}`;
    }
    if (!config) {
      config = {};
    }
    return UInstance.handleResponse(this.instance.get(url, config), true);
  }

  delete(url, query, config) {
    if (query) {
      url += `?${UInstance.serialize(query)}`;
    }
    if (!config) {
      config = {};
    }
    return UInstance.handleResponse(this.instance.delete(url, config), true);
  }

  post(url, query, config, silent) {
    if (!config) {
      config = {};
    }
    // eslint-disable-next-line max-len
    return UInstance.handleResponse(this.instance.post(url, query, config), silent);
  }
}

// eslint-disable-next-line import/no-mutable-exports
let http = null;
export default boot(({ app, store }) => {
  http = new UInstance('http://localhost:8092/api', {
    headers: {
      'Content-Type': 'application/json',
    },
  }, store);

  app.config.globalProperties.$http = http;
});

export { http };
