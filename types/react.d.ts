declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}

declare module 'react' {
  export = React;
  export as namespace React;
  namespace React {
    interface Component<P = {}, S = {}> {}
    interface FunctionComponent<P = {}> {
      (props: P): any;
    }
    type FC<P = {}> = FunctionComponent<P>;
    function createElement(type: any, props?: any, ...children: any[]): any;
  }
}
