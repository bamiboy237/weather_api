self.addEventListener('install', (event) => {
    event.waitUntil(
      caches.open('weather-pwa').then((cache) => {
        return cache.addAll([
          '/',
          '/index',
          '/weather',
          '/static/css/bootstrap.min.css',
          '/static/css/style.css',
          '/static/js/jquery-3.3.1.slim.min.js',
          '/static/js/popper.min.js',
          '/static/js/bootstrap.min.js',
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', (event) => {
    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request);
      })
    );
  });
  