import { render, screen } from '@testing-library/react';
import App from './App';
import fetchData from './containers/aboutMeContainer'

test('Check url', async () => {
  console.log("done");
  let res = await fetchData();
  console.log(res);
  expect(res).toEqual("cos")
});
