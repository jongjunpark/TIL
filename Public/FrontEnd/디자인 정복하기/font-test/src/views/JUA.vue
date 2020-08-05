<template>
  <div>
    <div class='thin'>
      <h1>H1, 안녕하세요.</h1>
      <h2>H2, 안녕하세요.</h2>
      <h3>H3, 안녕하세요.</h3>
      <h4>H4, 안녕하세요.</h4>
      <h5>H5, 안녕하세요.</h5>
      <h6>H6, 안녕하세요.</h6>
      <p class="f100">Font(100) 안녕하세요</p>
      <p class="f200">Font(200) 안녕하세요</p>
      <p class="f300">Font(300) 안녕하세요</p>
      <p class="f400">Font(400) 안녕하세요</p>
      <p class="f500">Font(500) 안녕하세요</p>
      <p class="f600">Font(600) 안녕하세요</p>
      <p class="f700">Font(700) 안녕하세요</p>
      <p class="f800">Font(800) 안녕하세요</p>
      <p class="f900">Font(900) 안녕하세요</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JUA'
}
</script>

<style scoped>
@font-face { font-family: 'BMJUA'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff') format('woff'); font-weight: normal; font-style: normal; }
.thin {
  font-family: 'BMJUA';
}
.f100 {
  font-size: 70px;
  font-weight: 100;
}

.f200 {
  font-size: 70px;
  font-weight: 200;
}

.f300 {
  font-size: 70px;
  font-weight: 300;
}

.f400 {
  font-size: 70px;
  font-weight: 400;
}

.f500 {
  font-size: 70px;
  font-weight: 500;
}

.f600 {
  font-size: 70px;
  font-weight: 600;
}

.f700 {
  font-size: 70px;
  font-weight: 700;
}

.f800 {
  font-size: 70px;
  font-weight: 800;
}

.f900 {
  font-size: 70px;
  font-weight: 900;
}
</style>