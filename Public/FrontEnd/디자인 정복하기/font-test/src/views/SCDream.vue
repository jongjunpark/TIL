<template>
  <div>
    <div class='thin'>
      <h1>Thin(100), 안녕하세요.</h1>
      <h2>Thin(100), 안녕하세요.</h2>
      <h3>Thin(100), 안녕하세요.</h3>
      <h4>Thin(100), 안녕하세요.</h4>
      <h5>Thin(100), 안녕하세요.</h5>
      <h6>Thin(100), 안녕하세요.</h6>
    </div>
    <div class='regular'>
      <h1>Regular(400), 안녕하세요.</h1>
      <h2>Regular(400), 안녕하세요.</h2>
      <h3>Regular(400), 안녕하세요.</h3>
      <h4>Regular(400), 안녕하세요.</h4>
      <h5>Regular(400), 안녕하세요.</h5>
      <h6>Regular(400), 안녕하세요.</h6>
    </div>
    <div class='black'>
      <h1>Black(900), 안녕하세요.</h1>
      <h2>Black(900), 안녕하세요.</h2>
      <h3>Black(900), 안녕하세요.</h3>
      <h4>Black(900), 안녕하세요.</h4>
      <h5>Black(900), 안녕하세요.</h5>
      <h6>Black(900), 안녕하세요.</h6>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SCDream'
}
</script>

<style scoped>
@font-face { font-family: 'SCDream-thin'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-1Thin.woff') format('woff'); font-weight: 100; }
@font-face { font-family: 'SCDream'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-4Regular.woff') format('woff'); font-weight: 400; }
@font-face { font-family: 'SCDream-black'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-9Black.woff') format('woff'); font-weight: 900; }
.thin {
  font-family: 'SCDream-thin';
}
.regular {
  font-family: 'SCDream';
}
.black {
  font-family: 'SCDream-black'
}
</style>