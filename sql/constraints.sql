-- ===========================================================
-- Project: Restaurant Operations Intelligence Platform
-- Description: Adds business and data-quality constraints
-- ===========================================================

-- Branches
ALTER TABLE branches
ADD CONSTRAINT chk_branches_capacity
CHECK (seating_capacity IS NULL OR seating_capacity > 0);

ALTER TABLE branches
ADD CONSTRAINT chk_branches_hours
CHECK (
    opening_time IS NULL
    OR closing_time IS NULL
    OR opening_time < closing_time
);

ALTER TABLE branches
ADD CONSTRAINT chk_branches_status
CHECK (status IN ('Open', 'Closed', 'Renovation'));

-- Products
ALTER TABLE products
ADD CONSTRAINT chk_products_selling_price
CHECK (selling_price >= 0);

ALTER TABLE products
ADD CONSTRAINT chk_products_food_cost
CHECK (food_cost >= 0);

ALTER TABLE products
ADD CONSTRAINT chk_products_price_above_cost
CHECK (selling_price >= food_cost);

ALTER TABLE products
ADD CONSTRAINT chk_products_preparation_time
CHECK (preparation_time IS NULL OR preparation_time >= 0);

ALTER TABLE products
ADD CONSTRAINT chk_products_calories
CHECK (calories IS NULL OR calories >= 0);

ALTER TABLE products
ADD CONSTRAINT chk_products_size
CHECK (
    product_size IS NULL
    OR product_size IN ('Standard', 'Large', 'Regular', 'Single', 'Not Applicable')
);

ALTER TABLE products
ADD CONSTRAINT chk_products_menu_status
CHECK (menu_status IN ('Active', 'Seasonal', 'Discontinued'));

-- Orders
ALTER TABLE orders
ADD CONSTRAINT chk_orders_channel
CHECK (order_channel IN ('Dine-in', 'Takeaway', 'Delivery'));

ALTER TABLE orders
ADD CONSTRAINT chk_orders_customer_count
CHECK (customer_count IS NULL OR customer_count > 0);

ALTER TABLE orders
ADD CONSTRAINT chk_orders_discount
CHECK (discount_amount >= 0);

ALTER TABLE orders
ADD CONSTRAINT chk_orders_final_amount
CHECK (final_amount >= 0);

ALTER TABLE orders
ADD CONSTRAINT chk_orders_status
CHECK (
    order_status IN (
        'Placed',
        'Preparing',
        'Ready',
        'Completed',
        'Cancelled'
    )
);

-- Order items
ALTER TABLE order_items
ADD CONSTRAINT chk_order_items_quantity
CHECK (quantity > 0);

ALTER TABLE order_items
ADD CONSTRAINT chk_order_items_unit_price
CHECK (unit_price >= 0);

ALTER TABLE order_items
ADD CONSTRAINT chk_order_items_line_total
CHECK (line_total >= 0);

-- Employees
ALTER TABLE employees
ADD CONSTRAINT chk_employees_hourly_rate
CHECK (hourly_rate > 0);

ALTER TABLE employees
ADD CONSTRAINT chk_employees_type
CHECK (employment_type IN ('Full-time', 'Part-time', 'Temporary'));

ALTER TABLE employees
ADD CONSTRAINT chk_employees_status
CHECK (employment_status IN ('Active', 'On Leave', 'Left'));

-- Shifts
ALTER TABLE shifts
ADD CONSTRAINT chk_shifts_hours_worked
CHECK (hours_worked IS NULL OR hours_worked >= 0);

ALTER TABLE shifts
ADD CONSTRAINT chk_shifts_overtime
CHECK (overtime_hours >= 0);

ALTER TABLE shifts
ADD CONSTRAINT chk_shifts_status
CHECK (shift_status IN ('Scheduled', 'Completed', 'Absent', 'Sick', 'Holiday'));

-- Payments
ALTER TABLE payments
ADD CONSTRAINT chk_payments_amount
CHECK (payment_amount >= 0);

ALTER TABLE payments
ADD CONSTRAINT chk_payments_method
CHECK (
    payment_method IN (
        'Cash',
        'Card',
        'Apple Pay',
        'Google Pay',
        'Gift Card'
    )
);

ALTER TABLE payments
ADD CONSTRAINT chk_payments_status
CHECK (payment_status IN ('Pending', 'Completed', 'Failed', 'Refunded'));

-- Waste
ALTER TABLE waste_records
ADD CONSTRAINT chk_waste_quantity
CHECK (quantity > 0);

ALTER TABLE waste_records
ADD CONSTRAINT chk_waste_cost
CHECK (estimated_cost IS NULL OR estimated_cost >= 0);

ALTER TABLE waste_records
ADD CONSTRAINT chk_waste_reason
CHECK (
    waste_reason IN (
        'Expired',
        'Overproduction',
        'Preparation Error',
        'Customer Return',
        'Damaged',
        'Dropped'
    )
);

-- Customer feedback
ALTER TABLE customer_feedback
ADD CONSTRAINT chk_feedback_overall_rating
CHECK (overall_rating IS NULL OR overall_rating BETWEEN 1 AND 5);

ALTER TABLE customer_feedback
ADD CONSTRAINT chk_feedback_food_rating
CHECK (food_rating IS NULL OR food_rating BETWEEN 1 AND 5);

ALTER TABLE customer_feedback
ADD CONSTRAINT chk_feedback_service_rating
CHECK (service_rating IS NULL OR service_rating BETWEEN 1 AND 5);

ALTER TABLE customer_feedback
ADD CONSTRAINT chk_feedback_cleanliness_rating
CHECK (cleanliness_rating IS NULL OR cleanliness_rating BETWEEN 1 AND 5);

-- Service metrics
ALTER TABLE service_metrics
ADD CONSTRAINT chk_service_status
CHECK (service_status IN ('On Time', 'Delayed', 'Cancelled'));


