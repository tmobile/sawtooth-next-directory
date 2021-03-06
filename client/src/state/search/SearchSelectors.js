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


export const SearchSelectors = {
  browse: (state) => {
    const formatted = [[], [], [], []];
    const data = [
      ...state.search.packs || [],
      ...state.search.roles || [],
    ];
    data.forEach((item, index) => {
      formatted[index % 4].push(item);
    });
    return formatted;
  },
  people:       (state) => state.search.people,
  roles:        (state) => state.search.roles,
  searchInput:  (state) => state.search.searchInput,
  searchLimit:  (state) => state.search.searchLimit,
  searchStart:  (state) => state.search.searchStart,
  searchTypes:  (state) => state.search.searchTypes,
  showSearch:   (state) => state.search.showSearch,
  totalPages:   (state) => state.search.totalPages,
};
