import { createGlobalState } from "react-hooks-global-state";

const { setGlobalState, useGlobalState } = createGlobalState({
  globalEmail: "",
  globalPassword: "",
});


export { useGlobalState, setGlobalState };
