/* Copyright 2019 Contributors to Hyperledger Sawtooth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------- */


import {
  getToken,
  get,
  getUserId,
  set,
  setToken,
  setUserId,
  remove,
  removeToken,
  removeUserId } from './Storage';


describe('Storage Service', () => {

  test('get token', () => {
    getToken();
  });

  test('set token', () => {
    setToken('value');
  });

  test('remove token', () => {
    removeToken();
  });

  test('remove user', () => {
    removeUserId();
  });

});
