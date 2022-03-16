// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline',
    // '/css/django-pwa-app.css',
    '/static/home/images/logo/cashlogger_logo1x.png',
    '/static/home/images/logo/cashlogger_logo2x.png',
    '/static/home/images/logo/cashlogger_logo3x.png',
    '/static/home/images/logo/cashlogger_logo4x.png',
    '/static/home/images/logo/my_app_icon.png',
    '/static/home/images/logo/splash-640x640.png',
    // '/images/logo/icon-96x96.png',
    // '/images/logo/icon-128x128.png',
    // '/images/logo/icon-144x144.png',
    // '/images/logo/icon-152x152.png',
    // '/images/logo/icon-192x192.png',
    // '/images/logo/icon-384x384.png',
    // '/images/logo/icon-512x512.png',
    // '/static/images/logo/splash-640x1136.png',
    // '/static/images/logo/splash-750x1334.png',
    // '/static/images/logo/splash-1242x2208.png',
    // '/static/images/logo/splash-1125x2436.png',
    // '/static/images/logo/splash-828x1792.png',
    // '/static/images/logo/splash-1242x2688.png',
    // '/static/images/logo/splash-1536x2048.png',
    // '/static/images/logo/splash-1668x2224.png',
    // '/static/images/logo/splash-1668x2388.png',
    // '/static/images/logo/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});