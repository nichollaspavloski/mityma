import { Notify } from 'quasar';

export default async () => {
  Notify.registerType('error', {
    position: 'top-right',
    timeout: 3500,
    icon: 'error',
    progress: true,
    color: 'red',
    textColor: 'white',
    actions: [
      { label: 'Dismiss', color: 'white', handler: () => {} },
    ],
    multiLine: true,
  });

  Notify.registerType('warn', {
    position: 'top-right',
    timeout: 3500,
    icon: 'warning',
    progress: true,
    color: 'orange',
    textColor: 'black',
    actions: [
      { label: 'Dismiss', color: 'black', handler: () => {} },
    ],
    multiLine: true,
  });

  Notify.registerType('info', {
    position: 'top-right',
    timeout: 3500,
    icon: 'information',
    progress: true,
    color: 'white',
    textColor: 'black',
    actions: [
      { label: 'Dismiss', color: 'black', handler: () => {} },
    ],
    multiLine: true,
  });
};
