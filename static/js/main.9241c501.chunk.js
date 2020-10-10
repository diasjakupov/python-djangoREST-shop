(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{40:function(e,t,a){},43:function(e,t,a){e.exports=a(89)},70:function(e,t,a){},71:function(e,t,a){},87:function(e,t,a){},88:function(e,t,a){},89:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(23),o=a.n(c),i=a(1),s=a(2),l=a(5),u=a(4),p=a(7),m=a.n(p),d=a(16),f=a(26),h=a.n(f),v=function(){function e(){var t=this;Object(i.a)(this,e),this.base_url="http://127.0.0.1:8000/api/",this.verifyJWTToken=function(){var e=Object(d.a)(m.a.mark((function e(t){var a,n,r;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a={headers:{"Content-Type":"application/json"}},n={token:t},e.prev=2,e.next=5,h.a.post("http://127.0.0.1:8000/auth/jwt/verify/",n,a);case 5:return r=e.sent,e.abrupt("return",r.status);case 9:return e.prev=9,e.t0=e.catch(2),e.abrupt("return",401);case 12:case"end":return e.stop()}}),e,null,[[2,9]])})));return function(t){return e.apply(this,arguments)}}(),this.refreshToken=function(){var e=Object(d.a)(m.a.mark((function e(t){var a,n,r,c;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=t.replace(/"/g,""),n={headers:{"Content-Type":"application/json",Accept:"application/json"}},r={refresh:a},e.next=5,h.a.post("http://127.0.0.1:8000/auth/jwt/refresh/",r,n);case 5:return c=e.sent,e.abrupt("return",c);case 7:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),this.checkToken=function(){var e=Object(d.a)(m.a.mark((function e(a,n){var r,c;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.verifyJWTToken(a);case 2:if(r=e.sent,console.log(r),401!==r){e.next=11;break}return e.next=7,t.refreshToken(n);case 7:return c=e.sent,e.abrupt("return",c.data);case 11:return e.abrupt("return");case 12:case"end":return e.stop()}}),e)})));return function(t,a){return e.apply(this,arguments)}}(),this.getProfile=function(){var e=Object(d.a)(m.a.mark((function e(a,n){var r,c,o;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=a.replace(/"/g,""),c={headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(r),Accept:"application/json"}},console.log("ok"),e.prev=3,e.next=6,h.a.get("".concat(t.base_url,"profile/").concat(n,"/"),c);case 6:o=e.sent,console.log(o.data),e.next=13;break;case 10:e.prev=10,e.t0=e.catch(3),console.log("bad request");case 13:case"end":return e.stop()}}),e,null,[[3,10]])})));return function(t,a){return e.apply(this,arguments)}}(),this.getListOfItem=function(){var e=Object(d.a)(m.a.mark((function e(a){var n;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.getResource(a);case 2:return n=e.sent,e.next=5,n;case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),this.getProductByID=function(){var e=Object(d.a)(m.a.mark((function e(a){var n;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.getResource("products/".concat(a));case 2:return n=e.sent,e.next=5,n;case 5:return e.abrupt("return",e.sent);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()}return Object(s.a)(e,[{key:"getResource",value:function(){var e=Object(d.a)(m.a.mark((function e(t){var a;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("".concat(this.base_url).concat(t));case 2:if(!(a=e.sent).ok){e.next=9;break}return e.next=6,a.json();case 6:return e.abrupt("return",e.sent);case 9:throw new Error("oops");case 10:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()}]),e}(),b=a(8),g=function(e){return{type:"GET_CATEGORYLIST",data:e}},E=function(e){return{type:"GET_PRODUCTS",data:e}},O=function(){return{type:"PRODUCTS_LOADING"}},j=function(e){return{type:"GET_CERTAIN_PRODUCT",data:e}},y=function(e){return{type:"SET_JWT",data:e}},k=function(){return{type:"USER_LOADED_SUCCESS"}},w=function(){return{type:"USER_LOADED_FAIl"}},S=function(){return{type:"SUCCESS_LOGGED"}},N=a(10),C=a(17),T=(a(70),a(71),function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(s.a)(a,[{key:"render",value:function(){return r.a.createElement("div",{className:"loadingio-spinner-gear-zfq3yq834cr"},r.a.createElement("div",{className:"ldio-35k1mubifkn"},r.a.createElement("div",null,r.a.createElement("div",null),r.a.createElement("div",null),r.a.createElement("div",null),r.a.createElement("div",null),r.a.createElement("div",null),r.a.createElement("div",null))))}}]),a}(r.a.Component)),A=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(s.a)(a,[{key:"render",value:function(){var e=this.props.child;return r.a.createElement("div",{className:"cat-card"},r.a.createElement("span",{className:"cat-item cat-link",key:e},r.a.createElement("h6",null,e.title)),e.children.map((function(e,t){return r.a.createElement("span",{key:t,className:"d-block cat-link"},e.title)})))}}]),a}(n.Component),x=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).service=new v,e}return Object(s.a)(a,[{key:"componentDidMount",value:function(){var e=this;this.service.getListOfItem("category").then((function(t){return e.props.getListOfCategory(t)}))}},{key:"render",value:function(){var e=this.props,t=e.category;e.loading;return r.a.createElement("div",{className:"cat-list",id:"category"},t.map((function(e,t){return r.a.createElement(A,{child:e,key:t})})))}}]),a}(n.Component),I=Object(N.b)((function(e){return{category:e.MainPageReducer.category,loading:e.MainPageReducer.loading}}),(function(e){return Object(b.a)({getListOfCategory:g},e)}))(x),D=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={dropdown:!1},e}return Object(s.a)(a,[{key:"dropMenu",value:function(e){this.setState({dropdown:!this.state.dropdown}),console.log("from navbar"),e.preventDefault()}},{key:"render",value:function(){var e=this,t="category-menu";return this.state.dropdown&&(t+=" show-dropdown"),r.a.createElement("nav",{className:"navbar navbar-expand-lg navbar-dark bg-dark"},r.a.createElement(C.b,{to:"/"},r.a.createElement("span",{className:"navbar-brand"},"\u041c\u0430\u0433\u0430\u0437\u0438\u043d")),r.a.createElement("button",{className:"navbar-toggler",type:"button","data-toggle":"collapse","data-target":"#navbarSupportedContent","aria-controls":"navbarSupportedContent","aria-expanded":"false","aria-label":"Toggle navigation"},r.a.createElement("span",{className:"navbar-toggler-icon"})),r.a.createElement("div",{className:"collapse navbar-collapse",id:"navbarSupportedContent"},r.a.createElement("ul",{className:"navbar-nav mr-auto"},r.a.createElement("li",{className:"nav-item dropdown"},r.a.createElement("span",{className:"nav-link dropdown-toggle",onClick:function(t){return e.dropMenu(t)}},"Dropdown"),r.a.createElement("div",{className:t},r.a.createElement(I,null))),r.a.createElement("li",{className:"nav-item"},r.a.createElement("div",{className:"nav-link"},r.a.createElement(C.b,{to:"/profile"},r.a.createElement("svg",{width:"1em",height:"1em",viewBox:"0 0 16 16",className:"bi bi-basket-fill basket-icon",fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},r.a.createElement("path",{fillRule:"evenodd",d:"M5.071 1.243a.5.5 0 0 1 .858.514L3.383 6h9.234L10.07 1.757a.5.5 0 1 1 .858-.514L13.783 6H15.5a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5H15v5a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V9H.5a.5.5 0 0 1-.5-.5v-2A.5.5 0 0 1 .5 6h1.717L5.07 1.243zM3.5 10.5a.5.5 0 1 0-1 0v3a.5.5 0 0 0 1 0v-3zm2.5 0a.5.5 0 1 0-1 0v3a.5.5 0 0 0 1 0v-3zm2.5 0a.5.5 0 1 0-1 0v3a.5.5 0 0 0 1 0v-3zm2.5 0a.5.5 0 1 0-1 0v3a.5.5 0 0 0 1 0v-3zm2.5 0a.5.5 0 1 0-1 0v3a.5.5 0 0 0 1 0v-3z"})),"\u041c\u043e\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c: \u041d\u0438\u043a\u043d\u0435\u0439\u043c")))),r.a.createElement("form",{className:"form-inline my-2 my-lg-0"},r.a.createElement("input",{className:"form-control mr-sm-2",type:"search",placeholder:"Search","aria-label":"Search"}),r.a.createElement("button",{className:"btn btn-outline-success my-2 my-sm-0",type:"submit"},"Search"))))}}]),a}(r.a.Component),L=(a(40),function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(s.a)(a,[{key:"render",value:function(){return r.a.createElement("div",{className:"alert alert-warning",role:"alert"},"A simple warning alert\u2014check it out!")}}]),a}(r.a.Component)),_=a(25),R=a.n(_),U=a(6),P=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).SelectedItem=function(t){e.props.history.push("/products/".concat(t))},e}return Object(s.a)(a,[{key:"render",value:function(){var e=this,t={dots:!0,infinite:!0,speed:500,slidesToShow:1,slidesToScroll:1},a=this.props.data;return r.a.createElement("div",{className:"card col-md-3"},r.a.createElement("div",{className:"product-image"},r.a.createElement(R.a,t,a.images.map((function(e){return r.a.createElement("img",{src:"".concat(e.image),className:"card-img-top ",alt:"...",key:e})})))),r.a.createElement("div",{className:"card-body"},r.a.createElement("h5",{className:"card-title"},a.title),r.a.createElement("p",{className:"card-text"},"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ",a.category,"."),r.a.createElement("p",{className:"card-text"},"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e: ",a.available,"."),r.a.createElement("p",{className:"card-text"},"\u0426\u0435\u043d\u0430: ",a.price,"."),r.a.createElement("button",{href:"#",className:"btn btn-primary check-product-page",onClick:function(){return e.SelectedItem(a.pk)}},"Go somewhere")))}}]),a}(n.Component),G=Object(U.f)(P),M=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).service=new v,e}return Object(s.a)(a,[{key:"componentDidMount",value:function(){var e=this.props,t=e.loadingItemList,a=e.getListOfProducts;t(),this.service.getListOfItem("products").then((function(e){return a(e)})).catch(r.a.createElement(L,null))}},{key:"render",value:function(){var e=this.props,t=e.products;return e.loading?r.a.createElement(T,null):r.a.createElement("div",{className:"row products-list"},t.map((function(e,t){return r.a.createElement(G,{key:t,data:e})})))}}]),a}(n.Component),J=Object(N.b)((function(e){return{products:e.MainPageReducer.products,loading:e.MainPageReducer.loading}}),(function(e){return Object(b.a)({getListOfProducts:E,loadingItemList:O},e)}))(M),z=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){return Object(i.a)(this,a),t.apply(this,arguments)}return Object(s.a)(a,[{key:"render",value:function(){return r.a.createElement("div",{className:"container-fluid"},r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-md-3 col-12"},r.a.createElement("div",{className:"filter-menu"},r.a.createElement("svg",{width:"1em",height:"1em",viewBox:"0 0 16 16",className:"bi bi-funnel-fill",fill:"currentColor",xmlns:"http://www.w3.org/2000/svg"},r.a.createElement("path",{fillRule:"evenodd",d:"M1.5 1.5A.5.5 0 0 1 2 1h12a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.128.334L10 8.692V13.5a.5.5 0 0 1-.342.474l-3 1A.5.5 0 0 1 6 14.5V8.692L1.628 3.834A.5.5 0 0 1 1.5 3.5v-2z"})),r.a.createElement("span",{className:"text-primary filter"},"\u0424\u0438\u043b\u044c\u0442\u0440"))),r.a.createElement("div",{className:"col-md-9 col-12"},r.a.createElement(J,null))))}}]),a}(n.Component),H=(a(87),function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).service=new v,e}return Object(s.a)(a,[{key:"componentDidMount",value:function(){var e=this;this.props.loadingItemList(),this.service.getProductByID(this.props.itemid).then((function(t){return e.props.getDetailPageOfItem(t)}))}},{key:"render",value:function(){var e={dots:!0,infinite:!0,speed:500,slidesToShow:1,slidesToScroll:1,arrows:!1,autoplay:!0},t=this.props,a=t.detail_product;return t.loading?r.a.createElement(T,null):r.a.createElement("div",{className:"row detail-block "},r.a.createElement("div",{className:"col-md-3 col-12 detail-image-block "},r.a.createElement(R.a,e,a.images.map((function(e,t){return r.a.createElement("img",{src:"".concat(e.image),key:t,className:"detail-image"})})))),r.a.createElement("div",{className:"col-md-8 col-12"},r.a.createElement("h3",null,a.title),r.a.createElement("p",{className:"text-break"},a.description),r.a.createElement("h4",{className:"text-primary"},a.price,"$"),r.a.createElement("button",{className:"btn btn-primary"},"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u043a\u043e\u0440\u0437\u0438\u043d\u0443")))}}]),a}(n.Component)),W=Object(N.b)((function(e){return{detail_product:e.MainPageReducer.detail_product,loading:e.MainPageReducer.loading}}),(function(e){return Object(b.a)({getDetailPageOfItem:j,loadingItemList:O},e)}))(H);function B(e){var t=null;if(document.cookie&&""!==document.cookie)for(var a=document.cookie.split(";"),n=0;n<a.length;n++){var r=a[n].trim();if(r.substring(0,e.length+1)===e+"="){t=decodeURIComponent(r.substring(e.length+1));break}}return t}var F=function(){var e=Object(d.a)(m.a.mark((function e(t){var a;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=B("csrftoken"),e.next=3,fetch("http://127.0.0.1:8000/auth/jwt/create",{method:"POST",headers:{"Content-Type":"application/json","x-csrftoken":a},body:JSON.stringify({username:t.username,password:t.password})}).then((function(e){return e.json()})).then((function(e){localStorage.setItem("jwtToken",JSON.stringify(e.access)),localStorage.setItem("refreshToken",JSON.stringify(e.refresh))}));case 3:e.sent;case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),q=function(){var e=Object(d.a)(m.a.mark((function e(t){return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:localStorage.setItem("jwtToken",t);case 1:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),V=(a(88),function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={username:"",password:""},e}return Object(s.a)(a,[{key:"HandleSubmit",value:function(e){e.preventDefault();var t=this.state,a=t.username,n=t.password;F({username:a,password:n});var r=localStorage.getItem("jwtToken"),c=localStorage.getItem("refreshToken");this.props.setJWTToken({access:r,refresh:c})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"wrapper fadeInDown"},r.a.createElement("div",{id:"formContent"},r.a.createElement("div",{className:"fadeIn first"},r.a.createElement("img",{src:"http://danielzawadzki.com/codepen/01/icon.svg",id:"icon",alt:"User Icon"})),r.a.createElement("input",{type:"text",id:"login",className:"fadeIn second",name:"login",placeholder:"login",onChange:function(t){return e.setState({username:t.target.value})}}),r.a.createElement("input",{type:"text",id:"password",className:"fadeIn third",name:"login",placeholder:"password",onChange:function(t){return e.setState({password:t.target.value})}}),r.a.createElement("input",{type:"submit",className:"fadeIn fourth",value:"Log In",onClick:function(t){return e.HandleSubmit(t)}}),r.a.createElement("div",{id:"formFooter"},r.a.createElement("a",{className:"underlineHover",href:"#"},"Forgot Password?"))))}}]),a}(n.Component)),Y=Object(N.b)((function(e){return{isLogged:e.Auth.isLogged}}),(function(e){return Object(b.a)({USER_LOADED_SUCCESS:k,setJWTToken:y,USER_IS_LOGGED:S},e)}))(V),$=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).server=new v,e}return Object(s.a)(a,[{key:"componentDidMount",value:function(){var e=this.props,t=e.USER_LOADED_FAIL,a=e.USER_LOADED_SUCCESS;this.server.checkToken(localStorage.getItem("jwtToken"),localStorage.getItem("refreshToken")).then((function(e){q(e),a()})).catch((function(){return t()}))}},{key:"render",value:function(){return this.props.isAuth?r.a.createElement("span",null,"Hello from profile page number ",this.props.userId):r.a.createElement(U.a,{to:"/login"})}}]),a}(r.a.Component),K=Object(N.b)((function(e){return{isAuth:e.Auth.isAuth,isLogged:e.Auth.isLogged}}),(function(e){return Object(b.a)({USER_LOADED_FAIL:w,USER_LOADED_SUCCESS:k},e)}))(Object(U.f)($)),Q=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).api=new v,e}return Object(s.a)(a,[{key:"componentDidMount",value:function(){localStorage.getItem("jwtToken"),localStorage.getItem("refreshToken")}},{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(D,null),r.a.createElement(U.b,{path:"/",component:z,exact:!0}),r.a.createElement(U.b,{path:"/products/:id",render:function(e){var t=e.match.params.id;return r.a.createElement(W,{itemid:t})},exact:!0}),r.a.createElement(U.b,{path:"/login",component:Y,exact:!0}),r.a.createElement(U.b,{path:"/profile/:id",render:function(e){var t=e.match.params.id;return r.a.createElement(K,{userId:t})},exact:!0}))}}]),a}(r.a.Component),X=Object(N.b)((function(e){e.products,e.loading;return{jwt:e.jwt}}),(function(e){return Object(b.a)({setJWTToken:y},e)}))(Q),Z=a(9),ee={access:"",refresh:"",isAuth:!1,isLogged:!1},te=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:ee,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"SUCCESS_LOGGED":return Object(Z.a)(Object(Z.a)({},e),{},{isLogged:!0});case"USER_LOADED_SUCCESS":return Object(Z.a)(Object(Z.a)({},e),{},{isAuth:!0});case"USER_LOADED_FAIL":return Object(Z.a)(Object(Z.a)({},e),{},{isAuth:!1});case"SET_JWT":return Object(Z.a)(Object(Z.a)({},e),{},{access:t.data.access,refresh:t.data.refresh});default:return e}},ae={products:[],category:[],loading:!0,detail_product:{title:"",images:[]}},ne=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:ae,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"PRODUCTS_LOADING":return Object(Z.a)(Object(Z.a)({},e),{},{loading:!0});case"GET_PRODUCTS":return Object(Z.a)(Object(Z.a)({},e),{},{products:t.data,loading:!1});case"GET_CATEGORYLIST":return Object(Z.a)(Object(Z.a)({},e),{},{category:t.data,loading:!1});case"GET_CERTAIN_PRODUCT":return console.log(t.data,"reducer"),Object(Z.a)(Object(Z.a)({},e),{},{products:[],loading:!1,detail_product:t.data});default:return e}},re=Object(b.c)(Object(b.b)({Auth:te,MainPageReducer:ne}));console.log(re.getState());var ce=re,oe=function(e){Object(l.a)(a,e);var t=Object(u.a)(a);function a(){var e;Object(i.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={error:!1},e}return Object(s.a)(a,[{key:"componentDidCatch",value:function(){this.setState({error:!0})}},{key:"render",value:function(){return this.state.error?r.a.createElement(L,null):this.props.children}}]),a}(r.a.Component);o.a.render(r.a.createElement(N.a,{store:ce},r.a.createElement(C.a,null,r.a.createElement(oe,null,r.a.createElement(X,null)))),document.getElementById("root"))}},[[43,1,2]]]);
//# sourceMappingURL=main.9241c501.chunk.js.map