--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-12-03 11:44:58

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 16488)
-- Name: SSH; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "SSH";


ALTER SCHEMA "SSH" OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16490)
-- Name: ingredients; Type: TABLE; Schema: SSH; Owner: postgres
--

CREATE TABLE "SSH".ingredients (
    ingredient_id integer NOT NULL,
    ingredient_name text NOT NULL,
    fridge_item boolean
);


ALTER TABLE "SSH".ingredients OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16489)
-- Name: ingredients_ingredient_id_seq; Type: SEQUENCE; Schema: SSH; Owner: postgres
--

ALTER TABLE "SSH".ingredients ALTER COLUMN ingredient_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME "SSH".ingredients_ingredient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 16505)
-- Name: linking; Type: TABLE; Schema: SSH; Owner: postgres
--

CREATE TABLE "SSH".linking (
    recipe_id integer NOT NULL,
    ingredient_id integer NOT NULL
);


ALTER TABLE "SSH".linking OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16498)
-- Name: recipes; Type: TABLE; Schema: SSH; Owner: postgres
--

CREATE TABLE "SSH".recipes (
    recipe_id integer NOT NULL,
    recipe_name text NOT NULL,
    description text,
    prep_time time without time zone NOT NULL,
    cook_time time without time zone,
    servings integer NOT NULL,
    kcal integer NOT NULL,
    protein integer NOT NULL,
    "carbs(sugar)" text NOT NULL,
    "fat(saturates)" text NOT NULL,
    fibre integer NOT NULL,
    salt integer NOT NULL,
    instructions text NOT NULL
);


ALTER TABLE "SSH".recipes OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16497)
-- Name: recipes_recipe_id_seq; Type: SEQUENCE; Schema: SSH; Owner: postgres
--

ALTER TABLE "SSH".recipes ALTER COLUMN recipe_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME "SSH".recipes_recipe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4856 (class 0 OID 16490)
-- Dependencies: 218
-- Data for Name: ingredients; Type: TABLE DATA; Schema: SSH; Owner: postgres
--

COPY "SSH".ingredients (ingredient_id, ingredient_name, fridge_item) FROM stdin;
20	milk	t
33	sesame oil	f
4	bananas	t
6	gelatin	t
3	baking powder	f
5	rosemary	t
8	mustard	t
9	avocado oil	f
12	almonds	f
13	sage	t
14	pumpkin	f
18	sunflower oil	f
22	polenta	t
23	mint	t
24	gouda	t
25	cornstarch	f
27	tahini	t
28	lime	t
29	vegetable oil	f
30	pineapple	t
32	brown sugar	f
35	peanuts	f
38	dill	t
39	dates	f
40	leeks	t
43	parsley	t
48	barley	f
49	jam	t
50	pork	t
52	cheddar cheese	t
53	guacamole	t
55	coconut	f
56	chives	t
57	goat cheese	t
58	mascarpone	t
59	brussels sprouts	t
60	potatoes	f
61	anise	f
62	cloves	f
63	sweet corn	t
64	asparagus	t
65	beets	t
66	pasta sauce	t
67	chocolate chips	f
70	millet	f
71	basil	t
73	peas	t
75	evaporated milk	f
76	bread	f
77	chili sauce	t
78	couscous	f
79	canola oil	f
80	pasta	f
81	soy sauce	f
82	yeast	f
83	powdered sugar	f
84	provolone	t
86	whipping cream	t
87	zucchini	t
88	ricotta	t
1	bay leaves	t
280	mango chutney	t
281	white wine	f
282	double cream	t
283	steak	t
284	crème fraîche	t
285	apple cider	t
286	coleslaw	t
287	barbeque sauce	t
288	prosciutto	t
289	lasagna sheets	f
290	chicken stock	t
291	raspberry	t
292	oat milk	t
293	granola	f
294	pine nuts	f
295	cannellini beans	f
296	bacon	t
297	white cabbage	t
298	marjoram	t
299	pork sausages	t
300	breadcrumbs	f
301	red wine	f
16	spinach	t
181	oysters	t
146	butter	t
133	yogurt	t
31	lettuce	t
37	tomatoes	t
17	apples	t
54	carrots	t
46	strawberries	t
47	garlic	t
26	cucumber	t
121	mushrooms	t
51	blueberries	t
96	cream	t
91	cream cheese	t
110	mayonnaise	t
115	ketchup	t
19	pickles	t
7	tofu	t
42	pesto	t
45	shrimp	t
41	fish	t
182	mussels	t
183	crab meat	t
184	anchovies	t
185	sardines	t
186	salmon	t
187	tuna	t
188	swordfish	t
189	tilapia	t
190	halibut	t
191	mahi mahi	t
192	trout	t
193	venison	t
194	duck meat	t
195	lamb	t
196	rabbit meat	t
197	turkey	t
198	bison	t
199	goose	t
200	kale	t
201	swiss chard	t
202	collard greens	t
203	okra	t
204	jalapeño peppers	t
205	habanero peppers	t
206	ghost peppers	t
207	shallots	t
208	fennel bulb	t
44	cheese	t
152	chicken	t
127	eggs	t
135	salt	f
10	cumin	f
34	paprika	f
85	flour	f
119	sugar	f
15	vinegar	f
21	baking soda	f
2	almond butter	f
11	cinnamon	f
36	oats	f
92	chili powder	f
98	molasses	f
72	maple syrup	f
74	honey	f
137	vanilla extract	f
68	coriander	t
69	rice	f
89	sauerkraut	t
90	radishes	t
93	eggplant	t
94	vanilla beans	f
95	black pepper	f
97	tomato sauce	t
99	chili peppers	t
100	parmesan cheese	t
101	white pepper	f
102	cauliflower	t
103	ginger	f
104	coconut oil	f
105	hummus	t
106	icing sugar	f
107	nutmeg	f
108	squash	t
109	lentils	f
111	olive oil	f
112	quinoa	f
113	chickpeas	f
114	fennel	f
116	peanut butter	t
117	onions	t
118	cardamom	f
120	turmeric	f
122	green beans	t
123	miso	t
124	hot sauce	t
125	kimchi	t
126	oranges	f
128	lemon	t
129	peppers	t
130	granulated sugar	f
131	feta cheese	t
132	oregano	f
134	farro	f
136	thyme	t
138	broccoli	t
139	mozzarella cheese	t
140	watermelon	t
141	olives	t
142	salsa	t
143	seaweed	t
144	cashews	f
145	avocado	t
147	beef	t
148	cocoa powder	f
149	celery	t
150	raisins	f
151	condensed milk	f
153	walnuts	f
154	artichokes	t
155	arugula	t
156	bamboo shoots	t
157	caper berries	t
158	cherries	t
159	grapefruit	t
160	kiwifruit	t
161	mango	t
162	papaya	t
163	peaches	t
164	plums	t
165	pomegranate	t
166	rhubarb	t
167	snow peas	t
168	turnips	t
169	watercress	t
170	acorn squash	t
171	butternut squash	t
172	pecans	f
173	hazelnuts	f
174	macadamia nuts	f
175	quail eggs	t
176	duck eggs	t
177	prawns	t
178	scallops	t
179	lobster	t
180	clams	t
209	radicchio	t
210	endive	t
211	bok choy	t
212	savoy cabbage	t
213	daikon radish	t
214	ginger root	f
215	galangal	f
216	tamarind	f
217	kaffir lime leaves	t
218	lemongrass	f
219	water chestnuts	f
220	lotus root	f
221	seaweed nori	f
222	dried shiitake mushrooms	t
223	truffle oil	f
224	caviar	t
225	edamame	t
226	wasabi	t
227	mochi	t
228	miso paste	t
229	rice noodles	f
230	glass noodles	f
231	udon	f
232	soba noodles	f
233	ravioli	f
234	gnocchi	f
235	risotto	f
236	arborio rice	f
237	jasmine rice	f
238	basmati rice	f
239	wild rice	f
240	freekeh	f
241	spelt	f
242	teff	f
243	wheat bran	f
244	flaxseeds	f
245	chia seeds	f
246	hemp seeds	f
247	sunflower seeds	f
248	pumpkin seeds	f
249	sesame seeds	f
250	poppy seeds	f
251	quark cheese	t
252	pancetta	t
253	pecorino cheese	t
254	spaghetti	f
255	spice paste	t
256	greek yoghurt	t
257	spring onion	t
258	courgette	t
259	mangetout	t
260	hoisin sauce	t
261	beef mince	t
262	beef stock	t
263	coriander seeds	f
264	chilli flakes	f
265	corn flour	f
266	chocolate	t
267	white wine vinegar	f
268	tomato purée	t
269	vegetable stock	t
270	oyster sauce	t
271	bread flour	f
272	passata	t
273	chicken broth	t
274	marinara sauce	t
276	lamb mince	t
277	plain flour	f
278	Worcestershire sauce	t
279	curry powder	f
\.


--
-- TOC entry 4859 (class 0 OID 16505)
-- Dependencies: 221
-- Data for Name: linking; Type: TABLE DATA; Schema: SSH; Owner: postgres
--

COPY "SSH".linking (recipe_id, ingredient_id) FROM stdin;
1	100
1	127
1	47
1	146
1	135
1	95
1	252
1	253
1	254
2	18
2	47
2	68
2	103
2	117
2	152
2	255
3	18
3	47
3	63
3	81
3	103
3	129
3	257
3	258
3	259
3	260
4	10
4	18
4	28
4	34
4	37
4	47
4	95
4	117
4	131
4	132
4	145
4	261
4	262
4	263
4	264
4	265
5	3
5	20
5	85
5	106
5	119
5	127
5	137
5	146
5	148
5	266
6	31
6	47
6	100
6	110
6	111
6	152
6	184
6	267
7	76
7	146
7	52
8	1
8	37
8	54
8	111
8	117
8	119
8	149
8	268
8	269
9	33
9	47
9	54
9	69
9	73
9	81
9	117
9	127
9	146
9	257
9	270
10	111
10	128
10	146
10	186
11	37
11	47
11	71
11	82
11	100
11	111
11	135
11	139
11	271
11	272
12	47
12	69
12	95
12	99
12	117
12	129
12	135
12	139
12	261
12	273
12	274
13	29
13	95
13	111
13	117
13	136
13	184
13	262
13	1
13	276
13	277
13	278
13	20
13	60
13	95
13	127
13	146
14	29
14	54
14	60
14	73
14	102
14	127
14	279
14	280
15	43
15	45
15	47
15	95
15	99
15	111
15	128
15	135
15	146
15	281
16	43
16	80
16	100
16	107
16	111
16	146
16	152
16	282
17	8
17	43
17	47
17	111
17	117
17	121
17	146
17	262
17	283
17	284
18	8
18	32
18	34
18	47
18	50
18	76
18	95
18	110
18	117
18	135
18	285
18	286
18	287
19	107
19	111
19	139
19	261
19	262
19	272
19	288
19	289
20	47
20	71
20	76
20	93
20	95
20	100
20	111
20	127
20	132
20	135
20	139
20	274
20	277
21	54
21	117
21	128
21	136
21	146
21	152
21	277
21	290
22	60
22	111
23	20
23	29
23	119
23	127
23	128
23	277
24	20
24	29
24	72
24	119
24	127
24	137
24	146
24	277
25	11
25	20
25	76
25	106
25	127
25	137
25	146
25	282
26	2
26	12
26	46
26	51
26	72
26	157
26	160
26	173
26	291
26	292
26	293
27	23
27	26
27	37
27	43
27	71
27	112
27	113
27	117
27	131
27	132
27	136
27	141
27	294
28	26
28	37
28	111
28	117
28	131
28	132
28	141
29	37
29	47
29	54
29	71
29	80
29	100
29	111
29	117
29	132
29	149
29	200
29	252
29	268
29	269
29	1
29	295
30	20
30	43
30	60
30	117
30	136
30	146
30	180
30	1
30	277
30	282
30	296
31	69
31	111
31	117
31	127
31	268
31	276
31	297
31	298
32	37
32	43
32	71
32	111
32	117
32	119
32	127
32	254
32	261
32	299
32	300
32	301
33	5
33	47
33	66
33	80
33	88
33	95
33	97
33	100
33	111
33	117
33	129
33	135
33	139
33	261
33	274
34	14
34	76
34	111
34	117
34	248
34	269
35	11
35	17
35	85
35	86
35	119
35	127
35	146
35	277
\.


--
-- TOC entry 4858 (class 0 OID 16498)
-- Dependencies: 220
-- Data for Name: recipes; Type: TABLE DATA; Schema: SSH; Owner: postgres
--

COPY "SSH".recipes (recipe_id, recipe_name, description, prep_time, cook_time, servings, kcal, protein, "carbs(sugar)", "fat(saturates)", fibre, salt, instructions) FROM stdin;
1	Spaghetti Carbonara	Classic Italian pasta with a creamy sauce.	00:10:00	00:20:00	2	400	15	40(5)	10(3)	5	1	Cook pasta. Mix eggs and cheese. Combine with pasta and pancetta.
2	Chicken Curry	Spicy and flavorful chicken dish.	00:15:00	00:30:00	4	500	30	50(8)	15(4)	7	2	Cook chicken with spices. Add coconut milk and simmer. Serve with rice.
3	Vegetable Stir Fry	Quick and healthy stir-fried vegetables.	00:10:00	00:15:00	2	300	10	30(4)	5(1)	6	1	Stir-fry vegetables with soy sauce and garlic. Serve with noodles or rice.
4	Beef Tacos	Mexican tacos with seasoned beef.	00:15:00	00:20:00	4	450	25	35(6)	20(7)	4	2	Cook beef with spices. Assemble tacos with toppings.
5	Chocolate Cake	Rich and moist chocolate dessert.	00:20:00	00:40:00	8	600	5	50(25)	25(10)	3	1	Mix ingredients, bake in oven, and let cool before serving.
6	Caesar Salad	Crisp romaine lettuce with creamy Caesar dressing.	00:10:00	00:20:00	2	250	10	20(2)	10(3)	3	1	Chop lettuce and toss with dressing. Add croutons and cheese.
7	Grilled Cheese Sandwich	Crispy grilled sandwich with melted cheese.	00:10:00	00:20:00	1	400	15	30(4)	15(6)	2	2	Butter bread, add cheese, and grill until golden.
8	Tomato Soup	Warm tomato soup with herbs and spices.	00:10:00	00:20:00	2	200	5	15(2)	5(1)	3	1	Cook tomatoes with spices, blend, and serve hot.
9	Fried Rice	Fried rice with vegetables and soy sauce.	00:10:00	00:20:00	4	300	8	40(5)	15(4)	5	2	Stir-fry rice with vegetables, soy sauce, and garlic.
10	Pan-Seared Salmon	Seared salmon served with lemon butter sauce.	00:10:00	00:20:00	2	500	40	5(0)	20(7)	2	1	Pan-sear salmon with seasoning and serve with sauce.
11	Margherita Pizza	Classic pizza with tomato, basil, and mozzarella.	00:10:00	00:20:00	4	400	15	50(6)	10(3)	4	1	Spread tomato sauce, add cheese and bake pizza.
12	Stuffed Bell Peppers	Bell peppers stuffed with rice and ground meat.	00:10:00	00:20:00	4	350	20	30(4)	10(3)	5	2	Fill bell peppers with mixture, bake, and serve.
14	Vegetable Curry	Spicy vegetable curry served with rice or naan.	00:10:00	00:20:00	4	450	15	45(6)	10(3)	6	1	Cook vegetables with spices and serve with rice.
15	Shrimp Scampi	Juicy shrimp cooked in garlic butter sauce.	00:10:00	00:20:00	2	550	30	10(1)	20(6)	2	1	Cook shrimp in garlic butter and serve with pasta.
16	Chicken Alfredo	Creamy Alfredo pasta with grilled chicken.	00:10:00	00:20:00	4	700	40	50(8)	20(7)	4	2	Cook pasta and mix with creamy Alfredo sauce.
17	Beef Stroganoff	Hearty beef pasta dish with creamy sauce.	00:10:00	00:20:00	4	650	35	50(7)	20(6)	4	2	Cook beef with sauce and serve with pasta.
18	Pulled Pork Sandwich	Slow-cooked pork served in a sandwich bun.	00:10:00	00:20:00	2	500	20	40(6)	25(10)	3	2	Slow-cook pork and assemble in sandwich buns.
19	Lasagna	Layers of pasta, cheese, and meat sauce.	00:10:00	00:20:00	6	800	25	60(8)	25(10)	5	2	Layer pasta, meat sauce, and cheese, then bake.
20	Eggplant Parmesan	Baked eggplant with marinara sauce and cheese.	00:10:00	00:20:00	4	450	15	30(4)	10(3)	4	1	Bake eggplant with marinara sauce and cheese.
21	Roast Chicken	Juicy roast chicken with herbs and spices.	00:10:00	00:20:00	4	600	35	20(2)	20(6)	3	2	Roast chicken with herbs and serve hot.
22	Potato Wedges	Crispy potato wedges seasoned with herbs.	00:10:00	00:20:00	4	300	8	40(4)	15(4)	5	1	Cut potatoes, season, and bake until crispy.
23	Pancakes	Fluffy pancakes served with syrup and butter.	00:10:00	00:20:00	4	400	10	50(8)	15(6)	3	1	Mix batter and cook pancakes. Serve with syrup.
24	Waffles	Crispy waffles with fruit and whipped cream.	00:10:00	00:20:00	4	400	10	50(7)	20(7)	4	1	Mix batter and cook waffles. Add toppings.
25	French Toast	Thick French toast dusted with powdered sugar.	00:10:00	00:20:00	4	350	8	30(4)	15(6)	3	1	Dip bread in egg mixture and cook. Add syrup.
26	Smoothie Bowl	Smoothie with fruit, granola, and seeds.	00:10:00	00:20:00	1	250	5	30(5)	5(2)	3	1	Blend fruits, pour into a bowl, and add toppings.
27	Quinoa Salad	Healthy salad with quinoa and fresh vegetables.	00:10:00	00:20:00	2	350	10	35(6)	10(3)	5	1	Mix quinoa, vegetables, and dressing. Serve fresh.
28	Greek Salad	Greek-style salad with feta cheese and olives.	00:10:00	00:20:00	4	300	8	30(5)	8(2)	4	1	Chop vegetables and toss with olives and feta.
29	Minestrone Soup	Hearty vegetable soup with pasta.	00:10:00	00:20:00	6	200	7	20(4)	5(2)	6	1	Cook vegetables with pasta in broth. Serve hot.
30	Clam Chowder	Creamy clam chowder with potatoes and celery.	00:10:00	00:20:00	4	400	10	20(4)	20(7)	4	2	Cook clams with cream and serve warm.
31	Cabbage Rolls	Cabbage leaves stuffed with rice and meat.	00:10:00	00:20:00	4	400	20	30(4)	15(6)	4	2	Stuff cabbage leaves with meat and rice, then bake.
32	Meatballs	Juicy meatballs in marinara sauce.	00:10:00	00:20:00	4	500	30	20(3)	25(10)	4	2	Cook meatballs in sauce and serve with pasta.
33	Baked Ziti	Baked pasta with cheese and tomato sauce.	00:10:00	00:20:00	4	600	20	40(5)	25(10)	4	1	Mix pasta, sauce, and cheese. Bake until golden.
34	Pumpkin Soup	Warm pumpkin soup spiced with nutmeg.	00:10:00	00:20:00	4	300	5	20(4)	5(2)	3	1	Cook pumpkin, blend, and add spices for soup.
35	Apple Pie	Classic dessert with spiced apples in a crust.	00:10:00	00:20:00	6	450	5	40(5)	15(6)	3	1	Prepare apple filling, assemble, and bake pie.
13	Shepards Pie	Traditional dish with ground meat and mashed potatoes.	00:10:00	00:20:00	6	600	25	40(5)	15(6)	6	2	Cook meat, layer with potatoes, and bake.
\.


--
-- TOC entry 4865 (class 0 OID 0)
-- Dependencies: 217
-- Name: ingredients_ingredient_id_seq; Type: SEQUENCE SET; Schema: SSH; Owner: postgres
--

SELECT pg_catalog.setval('"SSH".ingredients_ingredient_id_seq', 301, true);


--
-- TOC entry 4866 (class 0 OID 0)
-- Dependencies: 219
-- Name: recipes_recipe_id_seq; Type: SEQUENCE SET; Schema: SSH; Owner: postgres
--

SELECT pg_catalog.setval('"SSH".recipes_recipe_id_seq', 1, false);


--
-- TOC entry 4705 (class 2606 OID 16496)
-- Name: ingredients ingredients_pkey; Type: CONSTRAINT; Schema: SSH; Owner: postgres
--

ALTER TABLE ONLY "SSH".ingredients
    ADD CONSTRAINT ingredients_pkey PRIMARY KEY (ingredient_id);


--
-- TOC entry 4707 (class 2606 OID 16504)
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: SSH; Owner: postgres
--

ALTER TABLE ONLY "SSH".recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id);


--
-- TOC entry 4708 (class 2606 OID 16513)
-- Name: linking ingredient_id; Type: FK CONSTRAINT; Schema: SSH; Owner: postgres
--

ALTER TABLE ONLY "SSH".linking
    ADD CONSTRAINT ingredient_id FOREIGN KEY (ingredient_id) REFERENCES "SSH".ingredients(ingredient_id) NOT VALID;


--
-- TOC entry 4709 (class 2606 OID 16508)
-- Name: linking recipe_id; Type: FK CONSTRAINT; Schema: SSH; Owner: postgres
--

ALTER TABLE ONLY "SSH".linking
    ADD CONSTRAINT recipe_id FOREIGN KEY (recipe_id) REFERENCES "SSH".recipes(recipe_id) NOT VALID;


-- Completed on 2024-12-03 11:44:59

--
-- PostgreSQL database dump complete
--

