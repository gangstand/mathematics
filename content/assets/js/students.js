const SELECTOR = '.what_material_text';
		const SELECTOR_TWO = '.material_img';
		const ANIMATE_CLASS_NAME = 'animated';

		const animate = element => (
			element.classList.add(ANIMATE_CLASS_NAME)
			);

		const isAnimated = element => (
			element.classList.contains(ANIMATE_CLASS_NAME)
			);

		const intersectionObserver = new IntersectionObserver((entries, observer) => {
			entries.forEach((entry) => {

				if (entry.intersectionRatio > 0) {
					animate(entry.target);
					observer.unobserve(entry.target);
				}
			});
		});

		const elements = [].filter.call(
			document.querySelectorAll(SELECTOR),
			element => !isAnimated(element, ANIMATE_CLASS_NAME)
			);

			elements.forEach((element) => intersectionObserver.observe(element));

		const animate_t = element => (
			element.classList.add(ANIMATE_CLASS_NAME)
			);

		const isAnimated_t = element => (
			element.classList.contains(ANIMATE_CLASS_NAME)
			);

		const intersectionObserver_t = new IntersectionObserver((entries, observer) => {
			entries.forEach((entry) => {

				if (entry.intersectionRatio > 0) {
					animate(entry.target);
					observer.unobserve(entry.target);
				}
			});
		});

		const elements_t = [].filter.call(
			document.querySelectorAll(SELECTOR_TWO),
			element => !isAnimated(element, ANIMATE_CLASS_NAME)
			);

			elements_t.forEach((element) => intersectionObserver.observe(element));