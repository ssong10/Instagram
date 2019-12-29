# Insta Clone Coding - Vue

## 기본 설치 작업

```bash
$ vue create insta
$ cd insta
$ npm run serve
```

### Vue axios 사용

```bash
$ npm install axios
```

### Vue router 사용

```bash
$ npm i vue-router
$ vue add router
>> y
```

### Vuex 사용하기 위한 폴더 설치

```bash
$ npm i vuex
$ vue add vuex
>> y
```

## Router

> routing 을 하기 위해선 src/router 폴더 내의 index.js 파일을 통하여 경로 지정을 해주어야 한다.

```javascript
const routers = [
    ...,
    { path : '/login',
    name : 'login',
    component: () => import ('../views/Login.vue')
	}
]
```



















### Vue 에서 console.log 사용하기

> package.json

```json
    "rules": {
      "no-console": "off"
    },
```

