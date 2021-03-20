## SPA

> SPA (Single Page Aplication)

- 기존 웹은 하나의 데이터가 변경되면 새로고침이 필요했다. 즉, 사소한 변화를 적용하려면 모든 데이터를 매번 다시 불러와야 했다. 상당히 비효율적.
- AJAX(Asynchronous Javascript And XML)의 등장으로 비동기통신이 가능해졌고 전체 페이지의 새로고침이 아닌 부분적인 변화를 적용시킬 수 있게 되었다.

## React의 등장

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/21bfbbb0-b814-4d0c-9a49-2833432df5f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210320T073954Z&X-Amz-Expires=86400&X-Amz-Signature=22f36a39a52944d1bbf9e7d6c47f2bca55fcd4538736142a6612673835bce966&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

*(출처 : [React 공식문서](https://ko.reactjs.org/))*

- 개발자들은 웹개발의 편의성을 위해 웹 개발 라이브러리/프레임워크를 만들어 왔다.

- React는 그 중에 하나로 페이스북에서 만들었다.

- React는 가상DOM을 활용해서 SPA를 구성하기 때문에 앱같은 웹인 웹-앱을 적응할 수 있다.

  - SPA에서 큰 DOM을 가지고 있고 변화가 발생하면 큰 DOM에 바로 적용하지 않는다. 그 이유는 그 큰 DOM을 재 렌더링 하는 것이 비용적으로 매우 비효율적.
  - 그래서 가상DOM에 적용한 다음 실제 DOM에 넘겨주어 필요한 부분만 수정하게 도와줌

  [React and the Virtual DOM](https://www.youtube.com/watch?v=muc2ZF0QIO4)

## 왜 React를 사용해야 하나?

1. 컴포넌트 단위로 구성
   - 유지보수에 용이
2. 페이스북의 개발과 많은 사용량
   - 큰 기어븐 꾸준한 변화를 적용해주며 많은 이용자에 의한 거대한 커뮤니티는 큰 도움이 된다
3. JavaScript로 구성된 언어
   - JavaScript만 잘해도 React는 먹고 들어간다.
4. JSX (JavaScript eXtension)
   - Vue를 사용할 때 React는 JSX에 의해 복잡해 보였다. 하지만 조금만 사용해보니 Vue는 클린하게 코드를 작성할 수 있는 것이지 편리한 것은 아니었다. 반면에 JSX는 HTML에 기본적인 이해만 있다면 매우 용이하고 편리한 언어로 사용할 수 있다. 그래도 직관성은 Vue가 좋긴 한것 같다.

## 다른 라이브러리/프레임워크와의 비교

*(출처 : https://dzone.com/articles/react-vs-angular-vs-vuejs-a-complete-comparison-gu)*

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/38b70a95-95f1-4057-bb3c-a13081f4806d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210320T074428Z&X-Amz-Expires=86400&X-Amz-Signature=8a76e30dc1dfdb1b5a12b048c40c9f639debfc3ee56605b833a4f0cb1cf2fc2f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/92753891-c927-4018-a04d-87addc17078a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210320T074558Z&X-Amz-Expires=86400&X-Amz-Signature=b7d9bfc62d7e3ec0395eb4db1d2fb12279532bea32b58fb0dcd373e06e349c7e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## 다양한 기능들

### Context

- 동일한 `props`를 여러 하위 컴포넌트에 전달하는 것은 번거롭다.
- `context`는 전역적으로 공유가 가능하다.
- 단, `context`를 사용하면 컴포넌트 재사용이 어려워진다.

```jsx
const ThemeContext = React.createContext('light');

class App extends React.Component {
  render() {
    // Provider를 이용해 하위 트리에 테마 값을 보내줍니다.
    return (
      <ThemeContext.Provider value="dark">
        <Toolbar />
      </ThemeContext.Provider>
    );
  }
}

function Toolbar() {
  return (
    <div>
      <ThemedButton />
    </div>
  );
}

class ThemedButton extends React.Component {
  // 현재 선택된 테마 값을 읽기 위해 contextType을 지정합니다.
  // React는 가장 가까이 있는 테마 Provider를 찾아 그 값을 사용할 것입니다.
  // 이 예시에서 현재 선택된 테마는 dark입니다.
  static contextType = ThemeContext;
  render() {
    return <Button theme={this.context} />;
  }
```

### Ref

- React에서는 DOM에 접근하는 방식을 제공해준다. (JS의 document.queryselector와 유사)
- ref를 생성한 후 엘리멘트에 부착하면 해당 엘리멘트에 접근할 수 있다.

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }
  render() {
    return <div ref={this.myRef} />;
  }
}
```

- 접근은 생성한 ref의 current를 통해 가능하다.

```jsx
const node = this.myRef.current;
```