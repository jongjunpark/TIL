<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/scdream">에스코어체</router-link> |
      <router-link to="/blackhansans">검은고딕</router-link> |
      <router-link to="/mon">몬소리체</router-link> |
      <router-link to="/notosans">Noto Sans</router-link> |
      <router-link to="/inklipquid">잉크립퀴드</router-link> |
      <router-link to="/enjoystory">즐거운이야기</router-link> |
      <router-link to="/jua">배민 주아체</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
